# TXGLabs

### Descrição

Ainda não temos uma Descrição :D

## Tutoriais

### Como compilar e instalar:
 - Instale as dependências necessárias:
    - meson
    - ninja
    - blueprint-compiler
 - Clone o repositório: `git clone https://github.com/TXG0Fk3/TXGLabs`
 - Acesse o diretório root do projeto: `cd TXGLabs`
 - Organize com: `meson setup build --prefix=/usr`
 - Compile com: `meson compile -C build`
 - Instale com: `meson install -C build`
 - Desinstale com: `cd build` e `sudo ninja uninstall`