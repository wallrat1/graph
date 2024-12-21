# -*- coding: utf-8 -*-
import configparser
from git import Repo
from graphviz import Source

def get_commits_with_file_hash(repo_path, file_hash):
    repo = Repo(repo_path)
    commits_with_file = []

    for commit in repo.iter_commits():
        print(f"Checking commit: {commit.hexsha}")
        parents = commit.parents
        if not parents:
            continue
        try:
            for diff in commit.diff(parents):
                if diff.a_blob and diff.a_blob.hexsha == file_hash:
                    commits_with_file.append(commit.hexsha)
                    break
        except Exception as e:
            print(f"Error processing commit {commit.hexsha}: {e}")

    all_commits = set(commits_with_file)
    for commit in commits_with_file:
        commit_obj = repo.commit(commit)
        for parent in commit_obj.parents:
            all_commits.add(parent.hexsha)

    return list(all_commits)

def visualize_graph(commits, repo_path):
    graph = "digraph {"
    for commit in commits:
        graph += f'"{commit}" ; '
    
    for commit in commits:
        commit_obj = Repo(repo_path).commit(commit)
        for parent in commit_obj.parents:
            graph += f'"{parent.hexsha}" -> "{commit}" ; '

    graph += "}"
    
    with open("graph.dot", "w") as f:
        f.write(graph)
    
    
    source = Source(graph)
    source.render("graph", format="png", cleanup=True)

    print("Graph saved as 'graph.png'.")

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    repo_path = config['DEFAULT']['repo_path']
    file_hash = config['DEFAULT']['file_hash']
    
    commits = get_commits_with_file_hash(repo_path, file_hash)
    print(f"Commits with file hash: {commits}")
    visualize_graph(commits, repo_path)

if __name__ == "__main__":
    main()
