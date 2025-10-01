import sys
from pathlib import Path

current_file_path = Path(__file__).resolve()
src_dir = current_file_path.parent.parent.parent
print(src_dir)

if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from my_utils.db_manager import DBManager
from accounts.data.user_manager import UserManager

UserManager.x