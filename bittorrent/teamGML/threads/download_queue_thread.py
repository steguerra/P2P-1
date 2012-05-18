__author__ = 'LucaFerrari MarcoBersani GiovanniLodi'

from threading import Thread
from custom_utils.logging import klog
from custom_utils.hashing import *
from custom_utils.sockets import *
from PyQt4.QtCore import QThread, SIGNAL
from managers.filesmanager import FilesManager
from threads.download_thread import DownloadThread
import random


DOWNLOAD_FOLDER = "downloads"
QUEUE_LENGTH = 5

class DownloadQueueThread(QThread):

    def __init__(self, file, request_emitter, ui_handler):
        super(DownloadQueueThread, self).__init__()
        self._file = file
        self._ui_handler = ui_handler
        self._request_emitter = request_emitter
        self._downloaded_parts = int(FilesManager.get_completed_file_parts_count(file.id))


        klog("Started queue system for files %s %s" %(self._file.filename, str(self._file.id)))

    def _completed_part(self, file_id, file_part):
        if file_id != self._file.id:
            return
        self._downloaded_parts += 1
        FilesManager.set_status_part_for_file(file_id, file_part, "completed")
        if self._downloaded_parts == self._file.parts_count:
            FilesManager.create_file_from_parts(self._file.id)
        else:
            klog("Part finished, starting the new part")

            parts = FilesManager.get_ordered_parts_number(self._file.id)
            peers = FilesManager.get_peers_for_file_part(self._file.id, parts[0])
            peer = peers[random.randrange(0,len(peers)-1)]
            self._request_emitter.download_part(peer.ip, peer.port, file_id, parts[0])



    def run(self):
        self.connect(self, SIGNAL("part_download_finished"), self._completed_part)
        parts = FilesManager.get_ordered_parts_number()
        for i in range(0, min(QUEUE_LENGTH, len(parts))):
            peers = FilesManager.get_peers_for_file_part()
            peer = None
            if len(peers) > 0:
                peer = peers[random.randrange(0,len(peers)-1)]
                self._request_emitter.download_part(peer.ip, peer.port, self._file.id, parts[i])
