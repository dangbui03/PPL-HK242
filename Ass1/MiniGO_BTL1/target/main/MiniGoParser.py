# Generated from main/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u0196\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\3")
        buf.write("\2\7\2^\n\2\f\2\16\2a\13\2\3\2\3\2\3\2\3\3\3\3\3\3\7\3")
        buf.write("i\n\3\f\3\16\3l\13\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4t\n\4")
        buf.write("\3\5\3\5\3\5\3\5\5\5z\n\5\3\5\5\5}\n\5\3\5\5\5\u0080\n")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\5\6\u0087\n\6\3\6\5\6\u008a\n\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\7\b\u0096\n\b")
        buf.write("\f\b\16\b\u0099\13\b\3\b\7\b\u009c\n\b\f\b\16\b\u009f")
        buf.write("\13\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\5\r\u00b3\n\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\7\16\u00bb\n\16\f\16\16\16\u00be\13")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u00c6\n\17\f\17")
        buf.write("\16\17\u00c9\13\17\3\20\3\20\3\20\3\20\3\20\3\20\7\20")
        buf.write("\u00d1\n\20\f\20\16\20\u00d4\13\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\7\21\u00dc\n\21\f\21\16\21\u00df\13\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\7\22\u00e7\n\22\f\22\16\22\u00ea")
        buf.write("\13\22\3\23\3\23\3\23\5\23\u00ef\n\23\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\5\24\u00fa\n\24\3\25\3\25")
        buf.write("\3\25\5\25\u00ff\n\25\3\25\3\25\5\25\u0103\n\25\3\25\5")
        buf.write("\25\u0106\n\25\3\26\3\26\5\26\u010a\n\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0115\n\27\3\30\3")
        buf.write("\30\5\30\u0119\n\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\5\33\u0125\n\33\3\33\3\33\3\33\5\33\u012a")
        buf.write("\n\33\3\33\3\33\5\33\u012e\n\33\3\33\3\33\3\33\3\33\5")
        buf.write("\33\u0134\n\33\3\33\3\33\3\33\5\33\u0139\n\33\3\33\3\33")
        buf.write("\5\33\u013d\n\33\5\33\u013f\n\33\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\35\3\35\3\35\5\35\u0149\n\35\3\35\3\35\3\36\3\36")
        buf.write("\5\36\u014f\n\36\3\36\3\36\3\36\3\36\5\36\u0155\n\36\5")
        buf.write("\36\u0157\n\36\3\37\3\37\3\37\3\37\3 \3 \5 \u015f\n \3")
        buf.write("!\3!\3\"\3\"\5\"\u0165\n\"\3#\3#\3$\3$\3%\3%\3%\3%\3%")
        buf.write("\3%\5%\u0171\n%\3&\3&\5&\u0175\n&\3&\3&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\5\'\u017e\n\'\3(\3(\3(\3(\3(\5(\u0185\n(\3)\3)")
        buf.write("\3*\3*\3+\3+\3,\3,\3-\5-\u0190\n-\3-\3-\3.\3.\3.\2\7\32")
        buf.write("\34\36 \"/\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$")
        buf.write("&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\2\b\3\2\33\34\3\2")
        buf.write("\35\37\4\2\32\32\34\34\3\2\16\21\3\2:=\3\2\30\31\2\u01a0")
        buf.write("\2_\3\2\2\2\4e\3\2\2\2\6s\3\2\2\2\bu\3\2\2\2\n\u0081\3")
        buf.write("\2\2\2\f\u008b\3\2\2\2\16\u0092\3\2\2\2\20\u00a0\3\2\2")
        buf.write("\2\22\u00a3\3\2\2\2\24\u00a5\3\2\2\2\26\u00ab\3\2\2\2")
        buf.write("\30\u00b2\3\2\2\2\32\u00b4\3\2\2\2\34\u00bf\3\2\2\2\36")
        buf.write("\u00ca\3\2\2\2 \u00d5\3\2\2\2\"\u00e0\3\2\2\2$\u00ee\3")
        buf.write("\2\2\2&\u00f9\3\2\2\2(\u0105\3\2\2\2*\u0109\3\2\2\2,\u0114")
        buf.write("\3\2\2\2.\u0118\3\2\2\2\60\u011a\3\2\2\2\62\u011d\3\2")
        buf.write("\2\2\64\u013e\3\2\2\2\66\u0140\3\2\2\28\u0145\3\2\2\2")
        buf.write(":\u0156\3\2\2\2<\u0158\3\2\2\2>\u015e\3\2\2\2@\u0160\3")
        buf.write("\2\2\2B\u0164\3\2\2\2D\u0166\3\2\2\2F\u0168\3\2\2\2H\u0170")
        buf.write("\3\2\2\2J\u0172\3\2\2\2L\u017d\3\2\2\2N\u0184\3\2\2\2")
        buf.write("P\u0186\3\2\2\2R\u0188\3\2\2\2T\u018a\3\2\2\2V\u018c\3")
        buf.write("\2\2\2X\u018f\3\2\2\2Z\u0193\3\2\2\2\\^\5X-\2]\\\3\2\2")
        buf.write("\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`b\3\2\2\2a_\3\2\2\2b")
        buf.write("c\5\4\3\2cd\7\2\2\3d\3\3\2\2\2ej\5\6\4\2fi\5\6\4\2gi\5")
        buf.write("X-\2hf\3\2\2\2hg\3\2\2\2il\3\2\2\2jh\3\2\2\2jk\3\2\2\2")
        buf.write("k\5\3\2\2\2lj\3\2\2\2mt\5\b\5\2nt\5\n\6\2ot\5\26\f\2p")
        buf.write("t\5\f\7\2qt\5\24\13\2rt\5\22\n\2sm\3\2\2\2sn\3\2\2\2s")
        buf.write("o\3\2\2\2sp\3\2\2\2sq\3\2\2\2sr\3\2\2\2t\7\3\2\2\2uv\7")
        buf.write("\23\2\2vy\78\2\2wx\7(\2\2xz\5\32\16\2yw\3\2\2\2yz\3\2")
        buf.write("\2\2z|\3\2\2\2{}\5> \2|{\3\2\2\2|}\3\2\2\2}\177\3\2\2")
        buf.write("\2~\u0080\7\66\2\2\177~\3\2\2\2\177\u0080\3\2\2\2\u0080")
        buf.write("\t\3\2\2\2\u0081\u0082\7\22\2\2\u0082\u0083\78\2\2\u0083")
        buf.write("\u0084\7(\2\2\u0084\u0086\5\32\16\2\u0085\u0087\5> \2")
        buf.write("\u0086\u0085\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0089\3")
        buf.write("\2\2\2\u0088\u008a\7\66\2\2\u0089\u0088\3\2\2\2\u0089")
        buf.write("\u008a\3\2\2\2\u008a\13\3\2\2\2\u008b\u008c\7\13\2\2\u008c")
        buf.write("\u008d\78\2\2\u008d\u008e\7\f\2\2\u008e\u008f\7\62\2\2")
        buf.write("\u008f\u0090\5\16\b\2\u0090\u0091\7\63\2\2\u0091\r\3\2")
        buf.write("\2\2\u0092\u0093\5\20\t\2\u0093\u009d\7\66\2\2\u0094\u0096")
        buf.write("\5X-\2\u0095\u0094\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0095")
        buf.write("\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u009a\3\2\2\2\u0099")
        buf.write("\u0097\3\2\2\2\u009a\u009c\5\20\t\2\u009b\u0097\3\2\2")
        buf.write("\2\u009c\u009f\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e")
        buf.write("\3\2\2\2\u009e\17\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a1")
        buf.write("\78\2\2\u00a1\u00a2\5> \2\u00a2\21\3\2\2\2\u00a3\u00a4")
        buf.write("\7\n\2\2\u00a4\23\3\2\2\2\u00a5\u00a6\7\13\2\2\u00a6\u00a7")
        buf.write("\78\2\2\u00a7\u00a8\7\r\2\2\u00a8\u00a9\7\62\2\2\u00a9")
        buf.write("\u00aa\7\63\2\2\u00aa\25\3\2\2\2\u00ab\u00ac\7\n\2\2\u00ac")
        buf.write("\27\3\2\2\2\u00ad\u00ae\5\32\16\2\u00ae\u00af\7\67\2\2")
        buf.write("\u00af\u00b0\5\30\r\2\u00b0\u00b3\3\2\2\2\u00b1\u00b3")
        buf.write("\5\32\16\2\u00b2\u00ad\3\2\2\2\u00b2\u00b1\3\2\2\2\u00b3")
        buf.write("\31\3\2\2\2\u00b4\u00b5\b\16\1\2\u00b5\u00b6\5\34\17\2")
        buf.write("\u00b6\u00bc\3\2\2\2\u00b7\u00b8\f\4\2\2\u00b8\u00b9\7")
        buf.write("&\2\2\u00b9\u00bb\5\34\17\2\u00ba\u00b7\3\2\2\2\u00bb")
        buf.write("\u00be\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2")
        buf.write("\u00bd\33\3\2\2\2\u00be\u00bc\3\2\2\2\u00bf\u00c0\b\17")
        buf.write("\1\2\u00c0\u00c1\5\36\20\2\u00c1\u00c7\3\2\2\2\u00c2\u00c3")
        buf.write("\f\4\2\2\u00c3\u00c4\7\'\2\2\u00c4\u00c6\5\36\20\2\u00c5")
        buf.write("\u00c2\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2")
        buf.write("\u00c7\u00c8\3\2\2\2\u00c8\35\3\2\2\2\u00c9\u00c7\3\2")
        buf.write("\2\2\u00ca\u00cb\b\20\1\2\u00cb\u00cc\5 \21\2\u00cc\u00d2")
        buf.write("\3\2\2\2\u00cd\u00ce\f\4\2\2\u00ce\u00cf\7\5\2\2\u00cf")
        buf.write("\u00d1\5 \21\2\u00d0\u00cd\3\2\2\2\u00d1\u00d4\3\2\2\2")
        buf.write("\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\37\3\2")
        buf.write("\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00d6\b\21\1\2\u00d6\u00d7")
        buf.write("\5\"\22\2\u00d7\u00dd\3\2\2\2\u00d8\u00d9\f\4\2\2\u00d9")
        buf.write("\u00da\t\2\2\2\u00da\u00dc\5\"\22\2\u00db\u00d8\3\2\2")
        buf.write("\2\u00dc\u00df\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de")
        buf.write("\3\2\2\2\u00de!\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e1")
        buf.write("\b\22\1\2\u00e1\u00e2\5$\23\2\u00e2\u00e8\3\2\2\2\u00e3")
        buf.write("\u00e4\f\4\2\2\u00e4\u00e5\t\3\2\2\u00e5\u00e7\5$\23\2")
        buf.write("\u00e6\u00e3\3\2\2\2\u00e7\u00ea\3\2\2\2\u00e8\u00e6\3")
        buf.write("\2\2\2\u00e8\u00e9\3\2\2\2\u00e9#\3\2\2\2\u00ea\u00e8")
        buf.write("\3\2\2\2\u00eb\u00ec\t\4\2\2\u00ec\u00ef\5$\23\2\u00ed")
        buf.write("\u00ef\5&\24\2\u00ee\u00eb\3\2\2\2\u00ee\u00ed\3\2\2\2")
        buf.write("\u00ef%\3\2\2\2\u00f0\u00fa\5(\25\2\u00f1\u00fa\5\60\31")
        buf.write("\2\u00f2\u00fa\5\62\32\2\u00f3\u00fa\5\64\33\2\u00f4\u00fa")
        buf.write("\5\66\34\2\u00f5\u00fa\58\35\2\u00f6\u00f7\7\64\2\2\u00f7")
        buf.write("\u00f8\78\2\2\u00f8\u00fa\7\65\2\2\u00f9\u00f0\3\2\2\2")
        buf.write("\u00f9\u00f1\3\2\2\2\u00f9\u00f2\3\2\2\2\u00f9\u00f3\3")
        buf.write("\2\2\2\u00f9\u00f4\3\2\2\2\u00f9\u00f5\3\2\2\2\u00f9\u00f6")
        buf.write("\3\2\2\2\u00fa\'\3\2\2\2\u00fb\u0106\5N(\2\u00fc\u0106")
        buf.write("\78\2\2\u00fd\u00ff\78\2\2\u00fe\u00fd\3\2\2\2\u00fe\u00ff")
        buf.write("\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0102\7\60\2\2\u0101")
        buf.write("\u0103\5\30\r\2\u0102\u0101\3\2\2\2\u0102\u0103\3\2\2")
        buf.write("\2\u0103\u0104\3\2\2\2\u0104\u0106\7\61\2\2\u0105\u00fb")
        buf.write("\3\2\2\2\u0105\u00fc\3\2\2\2\u0105\u00fe\3\2\2\2\u0106")
        buf.write(")\3\2\2\2\u0107\u010a\5\62\32\2\u0108\u010a\5(\25\2\u0109")
        buf.write("\u0107\3\2\2\2\u0109\u0108\3\2\2\2\u010a+\3\2\2\2\u010b")
        buf.write("\u010c\7\64\2\2\u010c\u010d\5\30\r\2\u010d\u010e\7\65")
        buf.write("\2\2\u010e\u0115\3\2\2\2\u010f\u0110\7\64\2\2\u0110\u0111")
        buf.write("\5\30\r\2\u0111\u0112\7\65\2\2\u0112\u0113\5,\27\2\u0113")
        buf.write("\u0115\3\2\2\2\u0114\u010b\3\2\2\2\u0114\u010f\3\2\2\2")
        buf.write("\u0115-\3\2\2\2\u0116\u0119\5L\'\2\u0117\u0119\3\2\2\2")
        buf.write("\u0118\u0116\3\2\2\2\u0118\u0117\3\2\2\2\u0119/\3\2\2")
        buf.write("\2\u011a\u011b\5*\26\2\u011b\u011c\5,\27\2\u011c\61\3")
        buf.write("\2\2\2\u011d\u011e\78\2\2\u011e\u011f\7\60\2\2\u011f\u0120")
        buf.write("\5.\30\2\u0120\u0121\7\61\2\2\u0121\63\3\2\2\2\u0122\u0125")
        buf.write("\5*\26\2\u0123\u0125\5\60\31\2\u0124\u0122\3\2\2\2\u0124")
        buf.write("\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127\7.\2\2")
        buf.write("\u0127\u0129\5\30\r\2\u0128\u012a\7\60\2\2\u0129\u0128")
        buf.write("\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u012b\3\2\2\2\u012b")
        buf.write("\u012d\5.\30\2\u012c\u012e\7\61\2\2\u012d\u012c\3\2\2")
        buf.write("\2\u012d\u012e\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0130")
        buf.write("\5\64\33\2\u0130\u013f\3\2\2\2\u0131\u0134\5*\26\2\u0132")
        buf.write("\u0134\5\60\31\2\u0133\u0131\3\2\2\2\u0133\u0132\3\2\2")
        buf.write("\2\u0134\u0135\3\2\2\2\u0135\u0136\7.\2\2\u0136\u0138")
        buf.write("\5\30\r\2\u0137\u0139\7\60\2\2\u0138\u0137\3\2\2\2\u0138")
        buf.write("\u0139\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013c\5.\30\2")
        buf.write("\u013b\u013d\7\61\2\2\u013c\u013b\3\2\2\2\u013c\u013d")
        buf.write("\3\2\2\2\u013d\u013f\3\2\2\2\u013e\u0124\3\2\2\2\u013e")
        buf.write("\u0133\3\2\2\2\u013f\65\3\2\2\2\u0140\u0141\5H%\2\u0141")
        buf.write("\u0142\7\62\2\2\u0142\u0143\5\30\r\2\u0143\u0144\7\63")
        buf.write("\2\2\u0144\67\3\2\2\2\u0145\u0146\78\2\2\u0146\u0148\7")
        buf.write("\62\2\2\u0147\u0149\5:\36\2\u0148\u0147\3\2\2\2\u0148")
        buf.write("\u0149\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014b\7\63\2")
        buf.write("\2\u014b9\3\2\2\2\u014c\u014e\5<\37\2\u014d\u014f\5X-")
        buf.write("\2\u014e\u014d\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0157")
        buf.write("\3\2\2\2\u0150\u0151\5<\37\2\u0151\u0152\7\67\2\2\u0152")
        buf.write("\u0154\5:\36\2\u0153\u0155\5X-\2\u0154\u0153\3\2\2\2\u0154")
        buf.write("\u0155\3\2\2\2\u0155\u0157\3\2\2\2\u0156\u014c\3\2\2\2")
        buf.write("\u0156\u0150\3\2\2\2\u0157;\3\2\2\2\u0158\u0159\78\2\2")
        buf.write("\u0159\u015a\7/\2\2\u015a\u015b\5\32\16\2\u015b=\3\2\2")
        buf.write("\2\u015c\u015f\5@!\2\u015d\u015f\5B\"\2\u015e\u015c\3")
        buf.write("\2\2\2\u015e\u015d\3\2\2\2\u015f?\3\2\2\2\u0160\u0161")
        buf.write("\t\5\2\2\u0161A\3\2\2\2\u0162\u0165\5D#\2\u0163\u0165")
        buf.write("\5F$\2\u0164\u0162\3\2\2\2\u0164\u0163\3\2\2\2\u0165C")
        buf.write("\3\2\2\2\u0166\u0167\78\2\2\u0167E\3\2\2\2\u0168\u0169")
        buf.write("\78\2\2\u0169G\3\2\2\2\u016a\u016b\5J&\2\u016b\u016c\5")
        buf.write("H%\2\u016c\u0171\3\2\2\2\u016d\u016e\5J&\2\u016e\u016f")
        buf.write("\5> \2\u016f\u0171\3\2\2\2\u0170\u016a\3\2\2\2\u0170\u016d")
        buf.write("\3\2\2\2\u0171I\3\2\2\2\u0172\u0174\7\64\2\2\u0173\u0175")
        buf.write("\7:\2\2\u0174\u0173\3\2\2\2\u0174\u0175\3\2\2\2\u0175")
        buf.write("\u0176\3\2\2\2\u0176\u0177\7\65\2\2\u0177K\3\2\2\2\u0178")
        buf.write("\u0179\5N(\2\u0179\u017a\7\67\2\2\u017a\u017b\5L\'\2\u017b")
        buf.write("\u017e\3\2\2\2\u017c\u017e\5N(\2\u017d\u0178\3\2\2\2\u017d")
        buf.write("\u017c\3\2\2\2\u017eM\3\2\2\2\u017f\u0185\5P)\2\u0180")
        buf.write("\u0185\5R*\2\u0181\u0185\5V,\2\u0182\u0185\5T+\2\u0183")
        buf.write("\u0185\5Z.\2\u0184\u017f\3\2\2\2\u0184\u0180\3\2\2\2\u0184")
        buf.write("\u0181\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0183\3\2\2\2")
        buf.write("\u0185O\3\2\2\2\u0186\u0187\t\6\2\2\u0187Q\3\2\2\2\u0188")
        buf.write("\u0189\79\2\2\u0189S\3\2\2\2\u018a\u018b\t\7\2\2\u018b")
        buf.write("U\3\2\2\2\u018c\u018d\7>\2\2\u018dW\3\2\2\2\u018e\u0190")
        buf.write("\7\3\2\2\u018f\u018e\3\2\2\2\u018f\u0190\3\2\2\2\u0190")
        buf.write("\u0191\3\2\2\2\u0191\u0192\7\4\2\2\u0192Y\3\2\2\2\u0193")
        buf.write("\u0194\7\27\2\2\u0194[\3\2\2\2-_hjsy|\177\u0086\u0089")
        buf.write("\u0097\u009d\u00b2\u00bc\u00c7\u00d2\u00dd\u00e8\u00ee")
        buf.write("\u00f9\u00fe\u0102\u0105\u0109\u0114\u0118\u0124\u0129")
        buf.write("\u012d\u0133\u0138\u013c\u013e\u0148\u014e\u0154\u0156")
        buf.write("\u015e\u0164\u0170\u0174\u017d\u0184\u018f")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\r'", "'\n'", "<INVALID>", "'if'", "'else'", 
                     "'for'", "'return'", "'func'", "'type'", "'struct'", 
                     "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
                     "'const'", "'var'", "'continue'", "'break'", "'range'", 
                     "'nil'", "'true'", "'false'", "'!'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "'||'", "'&&'", "'='", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'.'", "':'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "REL", "IF", 
                      "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                      "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                      "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", 
                      "TRUE", "FALSE", "NOT", "ADD", "MINUS", "MUL", "DIV", 
                      "MOD", "EQUAL", "DIFF", "LT", "GT", "LE", "GE", "OR", 
                      "AND", "ASSIGN", "ADD_ASSIGN", "MINUS_ASSIGN", "MULT_ASSIGN", 
                      "DIV_ASSIGN", "REM_ASSIGN", "DOT", "COLON", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                      "SEMI", "COMMA", "ID", "FLOAT_LIT", "DEC_LIT", "BIN_LIT", 
                      "OCT_LIT", "HEX_LIT", "STR_LIT", "BOOL_LIT", "WS", 
                      "LINE_COMMENT", "BLOCK_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_variable_decl = 3
    RULE_const_decl = 4
    RULE_struct_decl = 5
    RULE_struct_fields = 6
    RULE_struct_field = 7
    RULE_method_decl = 8
    RULE_interface_decl = 9
    RULE_func_decl = 10
    RULE_list_expr = 11
    RULE_expr = 12
    RULE_and_expr = 13
    RULE_rela_expr = 14
    RULE_add_expr = 15
    RULE_mul_expr = 16
    RULE_unary_expr = 17
    RULE_primary_expr = 18
    RULE_exprd = 19
    RULE_func_expr = 20
    RULE_index_operator = 21
    RULE_args = 22
    RULE_arr_element = 23
    RULE_func_call = 24
    RULE_method_call = 25
    RULE_arr_lit = 26
    RULE_struct_lit = 27
    RULE_list_field = 28
    RULE_field = 29
    RULE_types = 30
    RULE_primitive_types = 31
    RULE_composite_types = 32
    RULE_struct_type = 33
    RULE_interface_type = 34
    RULE_arr_type = 35
    RULE_arr_dim = 36
    RULE_literal_list = 37
    RULE_literals = 38
    RULE_int_lit = 39
    RULE_float_lit = 40
    RULE_bool_lit = 41
    RULE_str_lit = 42
    RULE_newline = 43
    RULE_nil_lit = 44

    ruleNames =  [ "program", "decllist", "decl", "variable_decl", "const_decl", 
                   "struct_decl", "struct_fields", "struct_field", "method_decl", 
                   "interface_decl", "func_decl", "list_expr", "expr", "and_expr", 
                   "rela_expr", "add_expr", "mul_expr", "unary_expr", "primary_expr", 
                   "exprd", "func_expr", "index_operator", "args", "arr_element", 
                   "func_call", "method_call", "arr_lit", "struct_lit", 
                   "list_field", "field", "types", "primitive_types", "composite_types", 
                   "struct_type", "interface_type", "arr_type", "arr_dim", 
                   "literal_list", "literals", "int_lit", "float_lit", "bool_lit", 
                   "str_lit", "newline", "nil_lit" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    REL=3
    IF=4
    ELSE=5
    FOR=6
    RETURN=7
    FUNC=8
    TYPE=9
    STRUCT=10
    INTERFACE=11
    STRING=12
    INT=13
    FLOAT=14
    BOOLEAN=15
    CONST=16
    VAR=17
    CONTINUE=18
    BREAK=19
    RANGE=20
    NIL=21
    TRUE=22
    FALSE=23
    NOT=24
    ADD=25
    MINUS=26
    MUL=27
    DIV=28
    MOD=29
    EQUAL=30
    DIFF=31
    LT=32
    GT=33
    LE=34
    GE=35
    OR=36
    AND=37
    ASSIGN=38
    ADD_ASSIGN=39
    MINUS_ASSIGN=40
    MULT_ASSIGN=41
    DIV_ASSIGN=42
    REM_ASSIGN=43
    DOT=44
    COLON=45
    LPAREN=46
    RPAREN=47
    LBRACE=48
    RBRACE=49
    LBRACK=50
    RBRACK=51
    SEMI=52
    COMMA=53
    ID=54
    FLOAT_LIT=55
    DEC_LIT=56
    BIN_LIT=57
    OCT_LIT=58
    HEX_LIT=59
    STR_LIT=60
    BOOL_LIT=61
    WS=62
    LINE_COMMENT=63
    BLOCK_COMMENT=64
    ERROR_CHAR=65
    UNCLOSE_STRING=66
    ILLEGAL_ESCAPE=67

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decllist(self):
            return self.getTypedRuleContext(MiniGoParser.DecllistContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__0 or _la==MiniGoParser.T__1:
                self.state = 90
                self.newline()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self.decllist()
            self.state = 97
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = MiniGoParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.decl()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0):
                self.state = 102
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                    self.state = 100
                    self.decl()
                    pass
                elif token in [MiniGoParser.T__0, MiniGoParser.T__1]:
                    self.state = 101
                    self.newline()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.variable_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.func_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 110
                self.struct_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 111
                self.interface_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 112
                self.method_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_variable_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_decl" ):
                return visitor.visitVariable_decl(self)
            else:
                return visitor.visitChildren(self)




    def variable_decl(self):

        localctx = MiniGoParser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(MiniGoParser.VAR)
            self.state = 116
            self.match(MiniGoParser.ID)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ASSIGN:
                self.state = 117
                self.match(MiniGoParser.ASSIGN)
                self.state = 118
                self.expr(0)


            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 121
                self.types()


            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 124
                self.match(MiniGoParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_const_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(MiniGoParser.CONST)
            self.state = 128
            self.match(MiniGoParser.ID)
            self.state = 129
            self.match(MiniGoParser.ASSIGN)
            self.state = 130
            self.expr(0)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 131
                self.types()


            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 134
                self.match(MiniGoParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def struct_fields(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_fieldsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl" ):
                return visitor.visitStruct_decl(self)
            else:
                return visitor.visitChildren(self)




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(MiniGoParser.TYPE)
            self.state = 138
            self.match(MiniGoParser.ID)
            self.state = 139
            self.match(MiniGoParser.STRUCT)
            self.state = 140
            self.match(MiniGoParser.LBRACE)
            self.state = 141
            self.struct_fields()
            self.state = 142
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_fieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Struct_fieldContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,i)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NewlineContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NewlineContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_fields

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_fields" ):
                return visitor.visitStruct_fields(self)
            else:
                return visitor.visitChildren(self)




    def struct_fields(self):

        localctx = MiniGoParser.Struct_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_struct_fields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.struct_field()
            self.state = 145
            self.match(MiniGoParser.SEMI)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.ID))) != 0):
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__0 or _la==MiniGoParser.T__1:
                    self.state = 146
                    self.newline()
                    self.state = 151
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 152
                self.struct_field()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field" ):
                return visitor.visitStruct_field(self)
            else:
                return visitor.visitChildren(self)




    def struct_field(self):

        localctx = MiniGoParser.Struct_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_struct_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(MiniGoParser.ID)
            self.state = 159
            self.types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = MiniGoParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_method_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(MiniGoParser.FUNC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_decl" ):
                return visitor.visitInterface_decl(self)
            else:
                return visitor.visitChildren(self)




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(MiniGoParser.TYPE)
            self.state = 164
            self.match(MiniGoParser.ID)
            self.state = 165
            self.match(MiniGoParser.INTERFACE)
            self.state = 166
            self.match(MiniGoParser.LBRACE)
            self.state = 167
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(MiniGoParser.FUNC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr" ):
                return visitor.visitList_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_expr(self):

        localctx = MiniGoParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list_expr)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.expr(0)
                self.state = 172
                self.match(MiniGoParser.COMMA)
                self.state = 173
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_expr(self):
            return self.getTypedRuleContext(MiniGoParser.And_exprContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.and_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 181
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 182
                    self.match(MiniGoParser.OR)
                    self.state = 183
                    self.and_expr(0) 
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class And_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rela_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Rela_exprContext,0)


        def and_expr(self):
            return self.getTypedRuleContext(MiniGoParser.And_exprContext,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_and_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd_expr" ):
                return visitor.visitAnd_expr(self)
            else:
                return visitor.visitChildren(self)



    def and_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.And_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_and_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.rela_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 197
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.And_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_expr)
                    self.state = 192
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 193
                    self.match(MiniGoParser.AND)
                    self.state = 194
                    self.rela_expr(0) 
                self.state = 199
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Rela_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Add_exprContext,0)


        def rela_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Rela_exprContext,0)


        def REL(self):
            return self.getToken(MiniGoParser.REL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_rela_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRela_expr" ):
                return visitor.visitRela_expr(self)
            else:
                return visitor.visitChildren(self)



    def rela_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Rela_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_rela_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.add_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Rela_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_rela_expr)
                    self.state = 203
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 204
                    self.match(MiniGoParser.REL)
                    self.state = 205
                    self.add_expr(0) 
                self.state = 210
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Add_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Mul_exprContext,0)


        def add_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Add_exprContext,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_add_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_expr" ):
                return visitor.visitAdd_expr(self)
            else:
                return visitor.visitChildren(self)



    def add_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Add_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_add_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.mul_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 219
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Add_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_expr)
                    self.state = 214
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 215
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 216
                    self.mul_expr(0) 
                self.state = 221
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Mul_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Unary_exprContext,0)


        def mul_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Mul_exprContext,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_mul_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_expr" ):
                return visitor.visitMul_expr(self)
            else:
                return visitor.visitChildren(self)



    def mul_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Mul_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_mul_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.unary_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 230
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Mul_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_expr)
                    self.state = 225
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 226
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 227
                    self.unary_expr() 
                self.state = 232
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Unary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Unary_exprContext,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def primary_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Primary_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_unary_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_expr" ):
                return visitor.visitUnary_expr(self)
            else:
                return visitor.visitChildren(self)




    def unary_expr(self):

        localctx = MiniGoParser.Unary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_unary_expr)
        self._la = 0 # Token type
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT, MiniGoParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.NOT or _la==MiniGoParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 234
                self.unary_expr()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.ID, MiniGoParser.FLOAT_LIT, MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.primary_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprd(self):
            return self.getTypedRuleContext(MiniGoParser.ExprdContext,0)


        def arr_element(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_elementContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def method_call(self):
            return self.getTypedRuleContext(MiniGoParser.Method_callContext,0)


        def arr_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_litContext,0)


        def struct_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_litContext,0)


        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primary_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_expr" ):
                return visitor.visitPrimary_expr(self)
            else:
                return visitor.visitChildren(self)




    def primary_expr(self):

        localctx = MiniGoParser.Primary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_primary_expr)
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.exprd()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.arr_element()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.func_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 241
                self.method_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 242
                self.arr_lit()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 243
                self.struct_lit()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 244
                self.match(MiniGoParser.LBRACK)
                self.state = 245
                self.match(MiniGoParser.ID)
                self.state = 246
                self.match(MiniGoParser.RBRACK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralsContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exprd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprd" ):
                return visitor.visitExprd(self)
            else:
                return visitor.visitChildren(self)




    def exprd(self):

        localctx = MiniGoParser.ExprdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_exprd)
        self._la = 0 # Token type
        try:
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ID:
                    self.state = 251
                    self.match(MiniGoParser.ID)


                self.state = 254
                self.match(MiniGoParser.LPAREN)
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.STR_LIT))) != 0):
                    self.state = 255
                    self.list_expr()


                self.state = 258
                self.match(MiniGoParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def exprd(self):
            return self.getTypedRuleContext(MiniGoParser.ExprdContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_expr" ):
                return visitor.visitFunc_expr(self)
            else:
                return visitor.visitChildren(self)




    def func_expr(self):

        localctx = MiniGoParser.Func_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_func_expr)
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.exprd()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def index_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = MiniGoParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_index_operator)
        try:
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(MiniGoParser.LBRACK)
                self.state = 266
                self.list_expr()
                self.state = 267
                self.match(MiniGoParser.RBRACK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.match(MiniGoParser.LBRACK)
                self.state = 270
                self.list_expr()
                self.state = 271
                self.match(MiniGoParser.RBRACK)
                self.state = 272
                self.index_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_list(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = MiniGoParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_args)
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.literal_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Func_exprContext,0)


        def index_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_element" ):
                return visitor.visitArr_element(self)
            else:
                return visitor.visitChildren(self)




    def arr_element(self):

        localctx = MiniGoParser.Arr_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_arr_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.func_expr()
            self.state = 281
            self.index_operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def args(self):
            return self.getTypedRuleContext(MiniGoParser.ArgsContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(MiniGoParser.ID)
            self.state = 284
            self.match(MiniGoParser.LPAREN)
            self.state = 285
            self.args()
            self.state = 286
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def args(self):
            return self.getTypedRuleContext(MiniGoParser.ArgsContext,0)


        def method_call(self):
            return self.getTypedRuleContext(MiniGoParser.Method_callContext,0)


        def func_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Func_exprContext,0)


        def arr_element(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_elementContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_call" ):
                return visitor.visitMethod_call(self)
            else:
                return visitor.visitChildren(self)




    def method_call(self):

        localctx = MiniGoParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 288
                    self.func_expr()
                    pass

                elif la_ == 2:
                    self.state = 289
                    self.arr_element()
                    pass


                self.state = 292
                self.match(MiniGoParser.DOT)
                self.state = 293
                self.list_expr()
                self.state = 295
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 294
                    self.match(MiniGoParser.LPAREN)


                self.state = 297
                self.args()
                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.RPAREN:
                    self.state = 298
                    self.match(MiniGoParser.RPAREN)


                self.state = 301
                self.method_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 303
                    self.func_expr()
                    pass

                elif la_ == 2:
                    self.state = 304
                    self.arr_element()
                    pass


                self.state = 307
                self.match(MiniGoParser.DOT)
                self.state = 308
                self.list_expr()
                self.state = 310
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 309
                    self.match(MiniGoParser.LPAREN)


                self.state = 312
                self.args()
                self.state = 314
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 313
                    self.match(MiniGoParser.RPAREN)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_type(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_typeContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_lit" ):
                return visitor.visitArr_lit(self)
            else:
                return visitor.visitChildren(self)




    def arr_lit(self):

        localctx = MiniGoParser.Arr_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_arr_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.arr_type()
            self.state = 319
            self.match(MiniGoParser.LBRACE)
            self.state = 320
            self.list_expr()
            self.state = 321
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def list_field(self):
            return self.getTypedRuleContext(MiniGoParser.List_fieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_lit" ):
                return visitor.visitStruct_lit(self)
            else:
                return visitor.visitChildren(self)




    def struct_lit(self):

        localctx = MiniGoParser.Struct_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_struct_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(MiniGoParser.ID)
            self.state = 324
            self.match(MiniGoParser.LBRACE)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 325
                self.list_field()


            self.state = 328
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self):
            return self.getTypedRuleContext(MiniGoParser.FieldContext,0)


        def newline(self):
            return self.getTypedRuleContext(MiniGoParser.NewlineContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_field(self):
            return self.getTypedRuleContext(MiniGoParser.List_fieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_field" ):
                return visitor.visitList_field(self)
            else:
                return visitor.visitChildren(self)




    def list_field(self):

        localctx = MiniGoParser.List_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_list_field)
        try:
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.field()
                self.state = 332
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                if la_ == 1:
                    self.state = 331
                    self.newline()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.field()
                self.state = 335
                self.match(MiniGoParser.COMMA)
                self.state = 336
                self.list_field()
                self.state = 338
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                if la_ == 1:
                    self.state = 337
                    self.newline()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = MiniGoParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(MiniGoParser.ID)
            self.state = 343
            self.match(MiniGoParser.COLON)
            self.state = 344
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_types(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typesContext,0)


        def composite_types(self):
            return self.getTypedRuleContext(MiniGoParser.Composite_typesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = MiniGoParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_types)
        try:
            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.primitive_types()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.composite_types()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_types" ):
                return visitor.visitPrimitive_types(self)
            else:
                return visitor.visitChildren(self)




    def primitive_types(self):

        localctx = MiniGoParser.Primitive_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_primitive_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Composite_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_type(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_typeContext,0)


        def interface_type(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_composite_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite_types" ):
                return visitor.visitComposite_types(self)
            else:
                return visitor.visitChildren(self)




    def composite_types(self):

        localctx = MiniGoParser.Composite_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_composite_types)
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.struct_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.interface_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_type" ):
                return visitor.visitStruct_type(self)
            else:
                return visitor.visitChildren(self)




    def struct_type(self):

        localctx = MiniGoParser.Struct_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_struct_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_type" ):
                return visitor.visitInterface_type(self)
            else:
                return visitor.visitChildren(self)




    def interface_type(self):

        localctx = MiniGoParser.Interface_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_interface_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_dim(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_dimContext,0)


        def arr_type(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_typeContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_type" ):
                return visitor.visitArr_type(self)
            else:
                return visitor.visitChildren(self)




    def arr_type(self):

        localctx = MiniGoParser.Arr_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_arr_type)
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.arr_dim()
                self.state = 361
                self.arr_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.arr_dim()
                self.state = 364
                self.types()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_dimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def DEC_LIT(self):
            return self.getToken(MiniGoParser.DEC_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_dim

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_dim" ):
                return visitor.visitArr_dim(self)
            else:
                return visitor.visitChildren(self)




    def arr_dim(self):

        localctx = MiniGoParser.Arr_dimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_arr_dim)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(MiniGoParser.LBRACK)
            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.DEC_LIT:
                self.state = 369
                self.match(MiniGoParser.DEC_LIT)


            self.state = 372
            self.match(MiniGoParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralsContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def literal_list(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_list" ):
                return visitor.visitLiteral_list(self)
            else:
                return visitor.visitChildren(self)




    def literal_list(self):

        localctx = MiniGoParser.Literal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_literal_list)
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.literals()
                self.state = 375
                self.match(MiniGoParser.COMMA)
                self.state = 376
                self.literal_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.literals()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Int_litContext,0)


        def float_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Float_litContext,0)


        def str_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Str_litContext,0)


        def bool_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Bool_litContext,0)


        def nil_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Nil_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = MiniGoParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_literals)
        try:
            self.state = 386
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.int_lit()
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.float_lit()
                pass
            elif token in [MiniGoParser.STR_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 383
                self.str_lit()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 384
                self.bool_lit()
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 385
                self.nil_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEC_LIT(self):
            return self.getToken(MiniGoParser.DEC_LIT, 0)

        def BIN_LIT(self):
            return self.getToken(MiniGoParser.BIN_LIT, 0)

        def OCT_LIT(self):
            return self.getToken(MiniGoParser.OCT_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(MiniGoParser.HEX_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_int_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_lit" ):
                return visitor.visitInt_lit(self)
            else:
                return visitor.visitChildren(self)




    def int_lit(self):

        localctx = MiniGoParser.Int_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_int_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_float_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_lit" ):
                return visitor.visitFloat_lit(self)
            else:
                return visitor.visitChildren(self)




    def float_lit(self):

        localctx = MiniGoParser.Float_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_float_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(MiniGoParser.FLOAT_LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_bool_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_lit" ):
                return visitor.visitBool_lit(self)
            else:
                return visitor.visitChildren(self)




    def bool_lit(self):

        localctx = MiniGoParser.Bool_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_bool_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.TRUE or _la==MiniGoParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Str_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR_LIT(self):
            return self.getToken(MiniGoParser.STR_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_str_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStr_lit" ):
                return visitor.visitStr_lit(self)
            else:
                return visitor.visitChildren(self)




    def str_lit(self):

        localctx = MiniGoParser.Str_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_str_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(MiniGoParser.STR_LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_newline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline" ):
                return visitor.visitNewline(self)
            else:
                return visitor.visitChildren(self)




    def newline(self):

        localctx = MiniGoParser.NewlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_newline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.T__0:
                self.state = 396
                self.match(MiniGoParser.T__0)


            self.state = 399
            self.match(MiniGoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nil_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_nil_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNil_lit" ):
                return visitor.visitNil_lit(self)
            else:
                return visitor.visitChildren(self)




    def nil_lit(self):

        localctx = MiniGoParser.Nil_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_nil_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(MiniGoParser.NIL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expr_sempred
        self._predicates[13] = self.and_expr_sempred
        self._predicates[14] = self.rela_expr_sempred
        self._predicates[15] = self.add_expr_sempred
        self._predicates[16] = self.mul_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def and_expr_sempred(self, localctx:And_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def rela_expr_sempred(self, localctx:Rela_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def add_expr_sempred(self, localctx:Add_exprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def mul_expr_sempred(self, localctx:Mul_exprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




