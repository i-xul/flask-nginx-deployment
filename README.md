# flask-nginx-deployment

Example Flask application deployment using Nginx, uWSGI, and a self-hosted Linux server setup.

## Overview

This repository documents a practical deployment model for a Flask web application running behind Nginx on a self-hosted Linux server.

The goal of the project is to demonstrate how a lightweight Python web application can be served in a more production-oriented way using a WSGI server and reverse proxy instead of Flask's built-in development server.

## Current Scope

This repository includes:

* a minimal example Flask application
* uWSGI configuration for serving the app
* Nginx configuration for reverse proxying
* systemd service example for process management
* documentation for a simple self-hosted deployment workflow

## Features

* Flask application example
* Nginx reverse proxy setup
* uWSGI application serving
* systemd service management
* practical self-hosted deployment structure
* public portfolio version of a real deployment model

## Goals

* document a repeatable Flask deployment workflow
* show how application and infrastructure pieces connect together
* demonstrate a practical self-hosting stack
* create a reusable deployment example for future projects
* publish a sanitized version of a real-world setup

## Environment

* Linux server
* Python / Flask
* uWSGI
* Nginx
* systemd

## Notes

This repository is based on a real deployment approach adapted into a public example.

AI tools (ChatGPT) were used for idea exploration, debugging, and documentation support. The final setup pattern was tested and adjusted manually in a real environment.

Sensitive information such as real domains, IP addresses, file paths, and credentials has been removed from this public version.

## Integration Flow

The deployment model works as follows:

1. the Flask application provides the web routes
2. uWSGI runs the application as a long-lived service
3. systemd manages the uWSGI process
4. Nginx acts as a reverse proxy in front of the application
5. incoming requests are passed from Nginx to the uWSGI socket

This creates a more production-oriented setup than running the Flask development server directly.

## Repository Structure

- `app/` – minimal Flask application and Python requirements
- `uwsgi/` – uWSGI configuration
- `nginx/` – example Nginx reverse proxy configuration
- `systemd/` – example service definition
- `docs/` – project notes and documentation

## Next Steps

Possible future improvements:

- environment variable support
- static file handling examples
- HTTPS/TLS deployment notes
- example multi-app Nginx routing
- containerized deployment alternative
