Exec {
  path => [ "/usr/local/bin", "/usr/bin", "/bin" ]
}

node default {

  exec { "apt-update": command => "apt-get update" }
  Exec["apt-update"] -> Package <| |>

  include python
  include python::pillow

  package { "python-numpy":
    ensure => installed,
    require => Class[ "python" ],
  }

  package { "python-opencv":
    ensure => installed,
    require => [ Class[ "python" ], Package[ "python-numpy" ] ],
  }

  python::pip { "tornado":
    ensure => "3.1",
    require => Class[ "python" ],
  }

  python::pip { "coverage":
    ensure => "3.6",
    require => Class[ "python" ],
  }

  file { "/etc/init.d/pilbox":
    ensure => present,
    owner => "root",
    group => "root",
    mode => 0755,
    source => "/vagrant/puppet/files/etc/init.d/pilbox"
  }

  service { "pilbox":
    ensure => running,
    enable => true,
    hasrestart => true,
    hasstatus => true,
    require => [ File[ "/etc/init.d/pilbox" ],
                 Python::Pip[ "tornado" ],
                 Class[ "python::pillow" ] ]
  }

}
