# excecute kill me now on loop bash script
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin',
  onlyif  => 'pgrep killmenow',
}

