#Enable Holberton to login without errors

#Increase the hard nofile limit
exec { 'increase-hard-nofile-limit-for-user-Holberton':
  command => "sed -i '/^holberton *hard.*nofile/s/4/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}


#Increase the soft nofile limit
exec { 'increase-soft-nofile-limit-for-user-Holberton':
  command => "sed -i '/^holberton *soft/s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}
