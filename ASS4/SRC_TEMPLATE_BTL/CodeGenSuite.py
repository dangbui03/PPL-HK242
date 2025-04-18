"""
 * Initial code for Assignment
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/profile.php?id=100056605580171
 * Link Group : https://www.facebook.com/groups/211867931379013
 * Date: 02.04.2024
"""
import unittest
from TestUtils import TestCodeGen
import inspect
from AST import *

"""
    (cd java_byte_code/test_001 && 
    java  -jar ../jasmin.jar MiniGO.j && 
    java -cp ../_io:. MiniGO)
"""
class CodeGenSuite(unittest.TestCase):
    
    def test_001(self):
        """
func main() {
    putInt(1)
}
        """
        input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt",[IntLiteral(1)])]))])
        self.assertTrue(TestCodeGen.test(input, "1", inspect.stack()[0].function))    

    def test_002(self):
        """
func main() {
    putFloat(1.0)
}
        """
        input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putFloat",[FloatLiteral(1.0)])]))])
        self.assertTrue(TestCodeGen.test(input, "1.0", inspect.stack()[0].function))    