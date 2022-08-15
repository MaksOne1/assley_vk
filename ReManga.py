

from urllib import request


class ReManga(object):
    def __init__(self, settings):
        self.settings = settings
    
    def download_chapter():
        pass
    def get_all_chapters(self, branch_id):
        chapters = []
        # try:
        i = 1
        while True:
            req = request.get(
            self.settings['branch'].format(branch=branch_id, page=i), headers=self.settings['headers']).json()
            req_chapters = req['content']
            
            if not len(req_chapters):
                break

            for chapter in req_chapters:
                chapters.append(
                    {'id': chapter['id'], "index": chapter['chapter'], 'is_paid': chapter['is_paid']})
            
            i+=1
            
        return chapters

    def get_last_free_chapter(self, chapters):
        for chapter in chapters:
            if not chapter['is_paid']:
                return chapter
    
    def get_upload_status(self, vk_chapters, site_chapters):
        statuses = [
            'NOT_UPLOAD_IN_VK',
            'FULL_UPLOAD'
        ]
        
        if vk_chapters == site_chapters:
            return statuses[1]
        else:
            return statuses[0]
        
    
    