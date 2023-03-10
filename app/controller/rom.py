from db import connection
from flask import request
from datetime import datetime, timedelta


class ROM:
    def upload_rom(self):
        jenis = request.form['jenis']
        tanggal = request.form['tanggal']
        jumat1 = request.form['jumat1']
        sabtu1 = request.form['sabtu1']
        minggu1 = request.form['minggu1']
        senin1 = request.form['senin1']
        selasa1 = request.form['selasa1']
        rabu1 = request.form['rabu1']
        kamis1 = request.form['kamis1']
        jumat2 = request.form['jumat2']
        sabtu2 = request.form['sabtu2']
        minggu2 = request.form['minggu2']
        senin2 = request.form['senin2']
        selasa2 = request.form['selasa2']
        rabu2 = request.form['rabu2']
        kamis2 = request.form['kamis2']
        status1 = [jumat1,sabtu1,minggu1,senin1,selasa1,rabu1,kamis1]
        status2 = [jumat2,sabtu2,minggu2,senin2,selasa2,rabu2,kamis2]

        start_tanggal = datetime.strptime(tanggal, '%Y-%m-%d')
        if jenis == 'pltd':
            for i in range(len(status1)):
                new_tanggal = start_tanggal.strftime('%Y-%m-%d')
                self.insert_pltd(6, new_tanggal, status1[i])
                self.insert_pltd(7, new_tanggal, status2[i])
                start_tanggal += timedelta(days=1)
        elif jenis == 'pv':
            for i in range(len(status1)):
                new_tanggal = start_tanggal.strftime('%Y-%m-%d')
                self.insert_pv(1, new_tanggal, status1[i])
                self.insert_pv(2, new_tanggal, status2[i])
                start_tanggal += timedelta(days=1)
        elif jenis == 'bss':
            for i in range(len(status1)):
                new_tanggal = start_tanggal.strftime('%Y-%m-%d')
                self.insert_bss(1, new_tanggal, status1[i])
                self.insert_bss(2, new_tanggal, status2[i])
                start_tanggal += timedelta(days=1)

    def insert_pltd(self, unit, tanggal, status):
        query = f"INSERT INTO rompltd (unit, tanggal, status) VALUES ({unit}, '{tanggal}', {status})"
        connection(query, 'insert')

    def insert_pv(self, unit, tanggal, status):
        query = f"INSERT INTO rompv (unit, tanggal, status) VALUES ({unit}, '{tanggal}', {status})"
        connection(query, 'insert')

    def insert_bss(self, unit, tanggal, status):
        query = f"INSERT INTO rombss (unit, tanggal, status) VALUES ({unit}, '{tanggal}', {status})"
        connection(query, 'insert')

    def get_pltd(self, tanggal):
        query = f"SELECT * FROM rompltd WHERE tanggal = '{tanggal}'"
        result = connection(query, 'select')
        return result
    
    def get_pv(self, tanggal):
        query = f"SELECT * FROM rompv WHERE tanggal = '{tanggal}'"
        result = connection(query, 'select')
        return result
    
    def get_bss(self, tanggal):
        query = f"SELECT * FROM rombss WHERE tanggal = '{tanggal}'"
        result = connection(query, 'select')
        return result