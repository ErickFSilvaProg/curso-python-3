#!/bin/bash

# Atualizar pacotes
echo "Atualizando pacotes do sistema..."
sudo apt update && sudo apt upgrade -y

# Instalar dependências
echo "Instalando dependências para compilação do Python..."
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev \
libffi-dev liblzma-dev

# Baixar o Python 3.12.3
echo "Baixando Python 3.12.3..."
cd /tmp
wget https://www.python.org/ftp/python/3.12.3/Python-3.12.3.tgz

# Extrair e compilar
echo "Extraindo e compilando Python 3.12.3..."
tar -xvf Python-3.12.3.tgz
cd Python-3.12.3
./configure --enable-optimizations
make -j$(nproc)

# Instalar com altinstall
echo "Instalando Python 3.12.3 com altinstall..."
sudo make altinstall

# Verificar instalação
echo "Verificando instalação..."
/usr/local/bin/python3.12 --version

# Oferecer definir como padrão
echo ""
echo "Python 3.12.3 instalado com sucesso!"
echo "Se quiser usar python3 apontando para essa versão, rode:"
echo "  sudo update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.12 1"
echo "  sudo update-alternatives --config python3"
