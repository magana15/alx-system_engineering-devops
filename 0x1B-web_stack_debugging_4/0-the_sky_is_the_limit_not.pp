#Increase the ULIMIT of the default file
exec { 'fix-for-nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx && service nginx restart',
  path    => '/usr/local/bin:/bin:/usr/sbin:/usr/bin',
}
