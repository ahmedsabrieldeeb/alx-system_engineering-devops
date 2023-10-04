#!/usr/bin/env ruby
log = ARGV[0]

pattern = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

matches = log.scan(pattern)

if matches.any?
    matches.each do |match|
      from = match[0]
      to = match[1]
      flags = match[2]
      
      puts "#{from},#{to},#{flags}"
    end
else
    puts "Pattern not found in the input log."
end