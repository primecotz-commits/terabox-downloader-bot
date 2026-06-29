import os

# ===========================
# Telegram
# ===========================

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN_ID = int(os.getenv("ADMIN_ID", "5565826679"))

# ===========================
# Force Join
# ===========================

FORCE_JOIN = True

CHANNEL_USERNAME = "@Gezx_botz"

# ===========================
# Metadata
# ===========================

DEFAULT_ARTIST = "@Gezx_botz"

DEFAULT_ENCODER = "@Gezx_botz"

DEFAULT_COMMENT = "Downloaded by @Gezx_botz"

DEFAULT_AUTHOR = "@Gezx_botz"

# ===========================
# Download
# ===========================

MAX_FILE_SIZE = 2 * 1024 * 1024 * 1024  # 2GB

DOWNLOAD_FOLDER = "downloads"

TEMP_FOLDER = "temp"

# ===========================
# Queue
# ===========================

MAX_QUEUE = 5

MAX_DOWNLOADS = 2

# ===========================
# Progress
# ===========================

PROGRESS_UPDATE_TIME = 5

# ===========================
# Logging
# ===========================

LOG_CHANNEL = None

# ===========================
# Bot
# ===========================

BOT_NAME = "Gezx Downloader"

VERSION = "1.0"

# ===========================
# Database
# ===========================

DATABASE = "database.db"
