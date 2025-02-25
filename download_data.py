from sunpy.data.manager.storage import Storage

# Check all cached files
storage = manager.get_or_create_storage()
for file_info in storage:
    print(file_info.location)  # This prints the full path of each file
