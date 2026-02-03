#!/usr/bin/env bash
set -euo pipefail

apt-get update -y

# Installer Java 17 
apt-get install -y openjdk-17-jre-headless

# Installer Docker
# Source: https://docs.docker.com/engine/install/ubuntu/
apt-get install -y ca-certificates curl gnupg lsb-release coreutils

install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
   tee /etc/apt/sources.list.d/docker.list > /dev/null
apt-get update -y
apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

systemctl enable docker
systemctl start docker

# On attend que Docker soit opérationnel
until systemctl is-active --quiet docker && docker info >/dev/null 2>&1; do sleep 1; done

# Démarrer PostgreSQL dans un conteneur Docker
docker run -d \
  --name thingsboard-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=thingsboard \
  -p 5432:5432 \
  postgres:18

# https://manpages.ubuntu.com/manpages/noble/en/man8/shutdown.8.html
# Shutdown après 20 minutes
shutdown +20