conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', localedir)
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'txglabs.in',
  output: 'txglabs',
  configuration: conf,
  install: true,
  install_dir: bindir,
)