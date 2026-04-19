# Project Notes

## Purpose

This project was created to document a practical deployment pattern for Flask applications on a self-hosted Linux server.

The goal was to move beyond the Flask development server and use a more production-oriented stack built around uWSGI, Nginx, and systemd.

## What I learned

During this project I learned more about:

- structuring a Flask application for deployment
- serving Python web applications through uWSGI
- using Nginx as a reverse proxy
- managing application processes with systemd
- separating application code from deployment configuration
- adapting a real hosting model into a public portfolio example

## Practical lessons

One important lesson from this project was that even a simple web application benefits from a clear separation of concerns.

In this setup:

- Flask handles application logic
- uWSGI handles application serving
- Nginx handles incoming HTTP requests
- systemd handles process supervision

This makes the application easier to manage and better aligned with real-world deployment practices.

## Portfolio note

This repository is based on a real deployment approach adapted into a public example.

Sensitive information such as real paths, domains, and environment-specific details has been removed.

AI tools were used during development for ideation, debugging, and documentation, but the final setup pattern was tested and adapted manually in a real environment.
