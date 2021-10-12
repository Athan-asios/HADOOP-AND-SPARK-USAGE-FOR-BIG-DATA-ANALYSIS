#!/usr/bin/env python3

# ref: http://open.blogs.nytimes.com/2014/07/10/emr-streaming-in-go/

import sys
import json

def main():

    # loop through each line of stdin
    for line in sys.stdin:
        try:

            # parse the incoming json
            j = json.loads(line.strip())

            # initialize output structure
            output = dict()

            # grab an identifier
            output = j["authors"]
            if(len(output) > 1):
                #print(*output, sep = "  1\n", end = " ")
                for i in range(len(output)):
                   #separator = "  {}\n".format(i)
                   #print(output[i] + " => " + i)
                   print(output[i], end = "")
                   print("  {}\t1".format(i+1))
            else:
                print(*output, end = "  1\t1")



        except Exception as e:
            sys.stderr.write("unable to read log: %s" % e)
            continue




        try:

            # generate json output
            output_json = json.dumps(output)
            #output_json = output
            # write the key and json to stdout

            #print("{}\n".format(output_json))

        except Exception as e:
            sys.stderr.write("unable to write mapper output: %s" % e)
            continue


if __name__ == "__main__":
        main()
