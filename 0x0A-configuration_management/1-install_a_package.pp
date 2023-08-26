# Install puppet flask from pip3
package { 'flask':
  ensure   => 'present',
  provider => 'pip3'
  version  => '2.1.0',
}
