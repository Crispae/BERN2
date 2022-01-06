class CellLineNormalizer(object):
    def __init__(self, dict_path):
        self.NO_ENTITY_ID = 'CUI-less'

        # Create dictionary for exact match
        self.cl2oid = dict()
        with open(dict_path, 'r', encoding='utf-8') as f:
            for line in f:
                oid, names = line[:-1].split('||')
                names = names.split('|')
                for name in names:
                    self.cl2oid[name] = oid

    def normalize(self, names):
        oids = list()
        for name in names:
            if name in self.cl2oid:
                oids.append(self.cl2oid[name])
            elif name.lower() in self.cl2oid:
                oids.append(self.cl2oid[name.lower()])
            else:
                oids.append(self.NO_ENTITY_ID)
        
        return oids