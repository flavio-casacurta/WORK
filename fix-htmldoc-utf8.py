#!/usr/bin/env python
# coding: utf-8
#
# Name   : fix-htmldoc-utf8
# Summary: Program to fix UTF-8 characters that HTMLDOC has messed
# Author : Aurelio Jargas www.aurelio.net/soft
# License: BSD
# Release: April, 2008
#
# HTMLDOC has no Unicode support, so when you try to use it in a UTF-8 file,
# all the special characters (not ASCII) will be incorrect in the resulting HTML.
# This program fixes this, restoring the original UTF-8 characters.
#
# Just use it as a filter (reads STDIN, results to STDOUT) or use the -w option
# fix the file in place.
#
# Examples:
#       cat myfile.html | fix-htmldoc-utf8 > myfile-ok.html
#       fix-htmldoc-utf8 myfile.html > myfile-ok.html
#       fix-htmldoc-utf8 -w myfile.html
#

import sys

# You can add new chars to this mapping, if needed.
# The first set are the ISO-8859-1 extended chars.
# The second set are the Unicode chars I've found on my keyboard.
#
mapping = """
�       &Acirc;&iexcl;
�       &Acirc;&cent;
�       &Acirc;&pound;
�       &Acirc;&curren;
�       &Acirc;&yen;
�       &Acirc;&brvbar;
�       &Acirc;&sect;
�       &Acirc;&uml;
�       &Acirc;&copy;
�       &Acirc;&ordf;
�       &Acirc;&laquo;
�       &Acirc;&not;
�       &Acirc;&reg;
�       &Acirc;&macr;
�       &Acirc;&deg;
�       &Acirc;&plusmn;
�       &Acirc;&sup2;
�       &Acirc;&sup3;
�       &Acirc;&acute;
�       &Acirc;&mu;
�       &Acirc;&para;
�       &Acirc;&middot;
�       &Acirc;&cedil;
�       &Acirc;&sup1;
�       &Acirc;&ordm;
�       &Acirc;&raquo;
�       &Acirc;&frac14;
�       &Acirc;&frac12;
�       &Acirc;&frac34;
�       &Acirc;&iquest;
�       &Atilde;\x80
�       &Atilde;\x81
�       &Atilde;\x82
�       &Atilde;\x83
�       &Atilde;\x84
�       &Atilde;\x85
�       &Atilde;\x86
�       &Atilde;\x87
�       &Atilde;\x88
�       &Atilde;\x89
�       &Atilde;\x8a
�       &Atilde;\x8b
�       &Atilde;\x8c
�       &Atilde;\x8d
�       &Atilde;\x8e
�       &Atilde;\x8f
�       &Atilde;\x90
�       &Atilde;\x91
�       &Atilde;\x92
�       &Atilde;\x93
�       &Atilde;\x94
�       &Atilde;\x95
�       &Atilde;\x96
�       &Atilde;\x97
�       &Atilde;\x98
�       &Atilde;\x99
�       &Atilde;\x9a
�       &Atilde;\x9b
�       &Atilde;\x9c
�       &Atilde;\x9d
�       &Atilde;\x9e
�       &Atilde;\x9f
�       &Atilde;&nbsp;
�       &Atilde;&iexcl;
�       &Atilde;&cent;
�       &Atilde;&pound;
�       &Atilde;&curren;
�       &Atilde;&yen;
�       &Atilde;&brvbar;
�       &Atilde;&sect;
�       &Atilde;&uml;
�       &Atilde;&copy;
�       &Atilde;&ordf;
�       &Atilde;&laquo;
�       &Atilde;&not;
�       &Atilde;&shy;
�       &Atilde;&reg;
�       &Atilde;&macr;
�       &Atilde;&deg;
�       &Atilde;&plusmn;
�       &Atilde;&sup2;
�       &Atilde;&sup3;
�       &Atilde;&acute;
�       &Atilde;&mu;
�       &Atilde;&para;
�       &Atilde;&middot;
�       &Atilde;&cedil;
�       &Atilde;&sup1;
�       &Atilde;&ordm;
�       &Atilde;&raquo;
�       &Atilde;&frac14;
�       &Atilde;&frac12;
�       &Atilde;&frac34;
�       &Atilde;&iquest;

?       &iuml;&pound;&iquest;
�       &acirc;\x84&cent;
�       &acirc;\x82&not;
�       &Atilde;&brvbar;
�       &Aring;\x92
=       &acirc;\x89&curren;
?       &acirc;\x89&nbsp;
=       &acirc;\x89&yen;
?       &iuml;&not;\x81
?       &iuml;&not;\x82
8       &acirc;\x88\x9e
�       &acirc;\x80&cent;
/       &acirc;\x81\x84
�       &acirc;\x89\x88
?       &acirc;\x97\x8a
?       &acirc;\x88\x91
?       &acirc;\x88\x8f
p       &Iuml;\x80
?       &acirc;\x88\x82
?       &acirc;\x88\x86
�       &AElig;\x92
O       &Icirc;&copy;
v       &acirc;\x88\x9a
?       &acirc;\x88&laquo;
�       &acirc;\x80&nbsp;
�       &acirc;\x80&iexcl;
i       &Auml;&plusmn;
�       &acirc;\x80&ordm;
�       &Euml;\x9a
?       &Euml;\x99
?       &Euml;\x87
?       &Euml;\x9d
?       &Euml;\x9b
�       &acirc;\x80\x98
�       &acirc;\x80\x99
�       &acirc;\x80\x9a
�       &acirc;\x80\x9c
�       &acirc;\x80\x9d
�       &acirc;\x80\x9e
�       &acirc;\x80&brvbar;
�       &acirc;\x80\x94
�       &acirc;\x80\x93

CHARSET=utf-8   CHARSET=iso-8859-1
CHARSET=utf-8   CHARSET=iso-iso-8859-1
"""

# Just a standard search & replace
def fixit(text):
        for pair in mapping.split('\n'):
                if not pair: continue
                repl, patt = pair.split('\t')
                text = text.replace(patt.strip(), repl.strip())
        return text

# User wants to save the file in place or not?
write_file = False
if len(sys.argv) > 1 and sys.argv[1] == '-w':
        write_file = True
        sys.argv.pop(1)

# The input files (if any)
files = sys.argv[1:]

if files:
        # Fix input files one by one
        for this_file in files:
                try:
                        # Read and fix
                        f = open(this_file, 'r')
                        fixed = fixit(f.read())
                        f.close()

                        # Save the file or show on STDOUT
                        if write_file:
                                f = open(this_file, 'w')
                                f.write(fixed)
                                f.close()
                                print "Fixed", this_file
                        else:
                                print fixed,
                except:
                        print "Error fixing", this_file
                        sys.exit(1)
else:
        # No input file, read from STDIN and send results to STDOUT
        print fixit(sys.stdin.read()),
