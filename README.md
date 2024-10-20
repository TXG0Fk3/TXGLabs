# LwUtils

### Descrição

Ainda não temos uma Descrição :D

## Tutoriais

### Como compilar e instalar:
 - Instale as dependências necessárias:
    - meson
    - ninja
    - blueprint-compiler
 - Clone o repositório: `git clone https://github.com/LW-Tech-Corporation/LwUtils.git`
 - Acesse o diretório root do projeto: `cd LwUtils`
 - Organize com: `meson setup build --prefix=/usr`
 - Compile com: `meson compile -C build`
 - Instale com: `meson install -C build`
 - Desinstale com: `cd build` e `sudo ninja uninstall`