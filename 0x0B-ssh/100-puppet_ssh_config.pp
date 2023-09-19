#!/usr/bin/env bash
# puppet to make changes to our congiguration

file { 'ect/ssh/ssh_config':
  ensure => present,

content =>"
	
	#SSH client congiguration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
