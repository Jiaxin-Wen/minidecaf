"""minidecaf 是个包所以使用相对 import，注意下面 main 之前的句点。"""
from .main import main
import sys

sys.exit(main(sys.argv))
