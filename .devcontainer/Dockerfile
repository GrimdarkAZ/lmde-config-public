FROM mcr.microsoft.com/devcontainers/python:3.11-bookworm

ENV PYTHONUNBUFFERED 1

# Ensure apt is in non-interactive to avoid prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies.
RUN apt-get -y update --no-install-recommends \
    && apt-get -y install --no-install-recommends \
    build-essential \
    curl \
    ca-certificates \
    apt-utils \
    dialog \
    git \
    vim \
    python3-apt \
    python3-pip \
    && apt-get autoremove -y \
    && apt-get clean -y

# Install Python3 requirements

ENV DEBIAN_FRONTEND=dialog

WORKDIR /workspace

COPY ["./requirements.txt", "/workspace/"]

COPY ["postCreateCommand.sh", "/workspace"]

#RUN pip install --user --upgrade pip



