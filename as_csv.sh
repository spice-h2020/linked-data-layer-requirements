#!/bin/bash

gh issue list --limit 1000 |cut -f3|sed -E 's/([^ ]+) As a ([^,]+), to ([^ ,]+),? (.*)$/\1,\2,\3,"\4"/'
