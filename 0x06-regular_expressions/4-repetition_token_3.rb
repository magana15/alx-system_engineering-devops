#!/usr/bin/env ruby
#this script accepts one argument and passes it to a regular expression matching method

puts ARGV[0].scan(/hbt*n/).join
