"""
 * Initial code for Assignment 3
 * file : testunile.py
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""

from antlr4 import *
from StaticError import *
from CodeGenerator import CodeGenerator
import sys
import os
import subprocess

class TestUtil:
    @staticmethod
    def makeSource(inputStr, inputfile):
        file = open(inputfile, "w")
        file.write(inputStr)
        file.close()
        return FileStream(inputfile)

class TestCodeGen:
    @staticmethod
    def test(input, expect, num):
        TestCodeGen.check(num, input)
        dest = open('output/' + num + ".txt", "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(num, asttree):
        codeGen = CodeGenerator()
        path = "java_byte_code/" +  num
        if not os.path.isdir(path):
            os.mkdir(path)
                    
        base_path = f"java_byte_code/{num}"
        jasmin_jar = "../jasmin.jar"
        miniGO_class = "MiniGO"
        output_file = f"output/{num}.txt"

        f = open(output_file, "w")
        try:
            codeGen.gen(asttree, path)

            subprocess.run(
                ["java", "-jar", jasmin_jar, f"{miniGO_class}.j"],
                cwd=base_path,
                stderr=subprocess.STDOUT,
                check=True
            )

            subprocess.run(
                ["java", "-cp", "../_io:.", miniGO_class],
                cwd=base_path,
                stdout=f,
                stderr=subprocess.STDOUT,
                timeout=10,
                check=True
            )
        except StaticError as e:
            f.write(str(e) + "\n")
        except subprocess.CalledProcessError as e:
            f.write(f"Subprocess error: {e}\n")
        except subprocess.TimeoutExpired as e:
            f.write(f"Timeout error: {e}\n")
        except Exception as e:
            f.write(f"Unexpected error: {e}\n")
