# Increase the hard nofile limit for the holberton user
exec { 'increase-hard-nofile-limit-for-user-Holberton':
  command => "sed -i '/^holberton *hard.*nofile/s/[0-9]\\+/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin:/bin:/usr/bin',
  unless  => "grep -E '^holberton *hard *nofile *50000' /etc/security/limits.conf",
}

# Increase the soft nofile limit for the holberton user
exec { 'increase-soft-nofile-limit-for-user-Holberton':
  command => "sed -i '/^holberton *soft.*nofile/s/[0-9]\\+/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin:/bin:/usr/bin',
  unless  => "grep -E '^holberton *soft *nofile *50000' /etc/security/limits.conf",
}

