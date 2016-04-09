import sys

from django.contrib.staticfiles import finders
from django.core.management import call_command
from django.core.management.base import BaseCommand

from watchdog.utils.dirsnapshot import DirectorySnapshot, DirectorySnapshotDiff


class Command(BaseCommand):

    def handle(self, *args, **options):
        snapshots = {}
        roots = self.find_static_roots()

        if not roots:
            self.write('No static roots has been found in your application')
            return

        for path in roots:
            snapshots[path] = DirectorySnapshot(path)

        start_message = 'Directories to watch:\n{}'.format('\n'.join(roots))
        self.write(start_message)

        events = ('files_created', 'files_deleted', 'files_modified', 'files_moved')
        try:
            while True:
                for path in roots:
                    snapshot = DirectorySnapshot(path)
                    diff = DirectorySnapshotDiff(snapshot, snapshots[path])
                    if any(getattr(diff, event) for event in events):
                        snapshots[path] = snapshot
                        self.write('Changes detected')
                        call_command('collectstatic', interactive=False)
        except KeyboardInterrupt:
            pass

    @staticmethod
    def find_static_roots():
        found_files = set()
        for finder in finders.get_finders():
            for path, storage in finder.list([]):
                found_files.add(storage.base_location)
        return found_files

    @staticmethod
    def write(message):
        sys.stdout.write('{}\n'.format(message))


