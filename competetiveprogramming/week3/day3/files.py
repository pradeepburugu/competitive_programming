import os
import hashlib

def find_duplicate_files(starting_directory):
    files = {}
    stack = [starting_directory]
    duplicates = []

    while len(stack):
        current = stack.pop()
        if os.path.isdir(current):
            for path in os.listdir(current):
                full = os.path.join(current, path)
                stack.append(full)
        else:
            file = sample_hash_file(current)
            lastedited = os.path.getmtime(current)
            if file in files:
                existinglast, existing_path = files[file]
                if lastedited > existinglast:
                    duplicates.append((current, existing_path))
                else:
                    duplicates.append((existing_path, current))
                    files[file] = (lastedited, current)
            else:
                files[file] = (lastedited, current)

    return duplicates
def sample_hash_file(path):
    readsample = 4000
    total = os.path.getsize(path)
    hasher = hashlib.sha512()

    with open(path, 'rb') as file:
        if total < readsample * 3:
            hasher.update(file.read())
        else:
            samples = (
                (total - readsample * 3) // 2
            )
            for offset_multiplier in range(3):
                start_of_sample = (offset_multiplier* (readsample + samples))
                file.seek(start_of_sample)
                sample = file.read(readsample)
                hasher.update(sample)

    return hasher.hexdigest()

print(find_duplicate_files('H:\\01_competitive programming\\testing'))