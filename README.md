# System-API

API for retrieving host system information via HTTP


## Prerequisites

Ubuntu 18.04


## Development

Install Docker and Docker Compose:

https://docs.docker.com/install/

https://docs.docker.com/compose/install/


Clone the repository:

    git clone https://github.com/haeringer/system-api.git && cd system-api

Run the development environment:

    docker-compose up --build

Access the application via http://localhost:5000.
The dev environment uses the Flask development server, which automatically
reloads when changes are made to the python source code.
