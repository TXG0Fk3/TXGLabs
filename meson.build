project('txglabs',
          version: '0.1.0',
    meson_version: '>= 0.62.0',
  default_options: [ 'warning_level=2', 'werror=false', ],
)

i18n = import('i18n')
gnome = import('gnome')

python = import('python')
py_installation = python.find_installation('python3')
if not py_installation.found()
    error('No valid python3 binary found')
else
    message('Found python3 binary')
endif

prefix = get_option('prefix') # /usr
bindir = get_option('bindir') # /bin
datadir = get_option('datadir') # /usr/share
pkgdatadir = join_paths(prefix, datadir, meson.project_name())
pythondir = py_installation.get_install_dir()
localedir = join_paths(prefix, get_option('localedir'))

subdir('data')
subdir('TXGLabs')
subdir('po')
subdir('bin')

gnome.post_install(
     glib_compile_schemas: true,
    gtk_update_icon_cache: true,
  update_desktop_database: true,
)
