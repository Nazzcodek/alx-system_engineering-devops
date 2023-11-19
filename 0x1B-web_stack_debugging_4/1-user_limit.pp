#Allow user 'holberton' to login and open file without error

# Hard file limit increase for user 'halberton'
exec { 'hard-file-limit':
  command => 'sed -i "/holberton hard/s/5/50645/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Soft file limit increase for user 'holberton'
exec { 'soft-file-limit':
  command => 'sed -i "/holberton soft/s/4/50645/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
