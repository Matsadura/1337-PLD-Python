#!/usr/bin/env python3
import json
import os
import subprocess

def get_projects():
    projects = json.load(open('projects.json'))
    projects_names = list(enumerate(projects.keys(), start=1))
    for i, project in projects_names:
        print(f'{i}. {project}')
    print('Select a project to open: ')
    project = int(input())
    project = projects_names[project - 1][1]
    print(f'Opening {project}...')
    return project

def list_project_tasks(project):
    projects = json.load(open('projects.json'))
    project_tasks = list(enumerate(projects[project]["Tasks"].keys(), start=1))
    print(f'Tasks for {project}:')
    for task in project_tasks:
        print(f'{task[0]}- {task[1]}')
    print('Select a task to open: ')
    task = int(input())
    task = project_tasks[task - 1][1]
    print(f'Opening {task}...')
    return task

def open_project_task(project, task):
    projects = json.load(open('projects.json'))
    task_path = projects[project]["Tasks"][task]
    subprocess.run(['clear'], check=True)
    subprocess.run(['glow', os.getcwd() + '/' + task_path], check=True)


if __name__ == '__main__':
    project = get_projects()
    task = list_project_tasks(project)
    open_project_task(project, task)