# deletion of a file manifest

exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/usr/bin/pgrep killmenow',
}