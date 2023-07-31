from db import connection
from flask import request
from datetime import datetime, timedelta, date


class ROM:
    def upload_rom(self):
        jenis = request.form["jenis"]
        tanggal = request.form["tanggal"]
        jumat1 = request.form["jumat1"]
        sabtu1 = request.form["sabtu1"]
        minggu1 = request.form["minggu1"]
        senin1 = request.form["senin1"]
        selasa1 = request.form["selasa1"]
        rabu1 = request.form["rabu1"]
        kamis1 = request.form["kamis1"]
        jumat2 = request.form["jumat2"]
        sabtu2 = request.form["sabtu2"]
        minggu2 = request.form["minggu2"]
        senin2 = request.form["senin2"]
        selasa2 = request.form["selasa2"]
        rabu2 = request.form["rabu2"]
        kamis2 = request.form["kamis2"]
        status1 = [jumat1, sabtu1, minggu1, senin1, selasa1, rabu1, kamis1]
        status2 = [jumat2, sabtu2, minggu2, senin2, selasa2, rabu2, kamis2]

        start_tanggal = datetime.strptime(tanggal, "%Y-%m-%d")
        if jenis == "pltd":
            if self.get_data_week(f"rom{jenis}", tanggal):
                self.delete_data_week(f"rom{jenis}", tanggal)
            for i in range(len(status1)):
                new_tanggal = start_tanggal.strftime("%Y-%m-%d")
                self.insert_pltd(6, new_tanggal, status1[i])
                self.insert_pltd(7, new_tanggal, status2[i])
                start_tanggal += timedelta(days=1)
        elif jenis == "pv":
            if self.get_data_week(f"rom{jenis}", tanggal):
                self.delete_data_week(f"rom{jenis}", tanggal)
            for i in range(len(status1)):
                new_tanggal = start_tanggal.strftime("%Y-%m-%d")
                self.insert_pv(1, new_tanggal, status1[i])
                self.insert_pv(2, new_tanggal, status2[i])
                start_tanggal += timedelta(days=1)
        elif jenis == "bss":
            if self.get_data_week(f"rom{jenis}", tanggal):
                self.delete_data_week(f"rom{jenis}", tanggal)
            for i in range(len(status1)):
                new_tanggal = start_tanggal.strftime("%Y-%m-%d")
                self.insert_bss(1, new_tanggal, status1[i])
                self.insert_bss(2, new_tanggal, status2[i])
                start_tanggal += timedelta(days=1)

    def auto_upload_rom(self, unit):
        status = 1
        today = datetime.now()
        if today.weekday() == 4:
            if self.check_rom(unit):
                pass
            else:
                if unit == "rompltd":
                    for i in range(7):
                        self.insert_pltd(6, today, status)
                        self.insert_pltd(7, today, status)
                        today += timedelta(days=1)
                elif unit == "rompv":
                    for i in range(7):
                        self.insert_pv(1, today, status)
                        self.insert_pv(2, today, status)
                        today += timedelta(days=1)
                elif unit == 'rombss':
                    for i in range(7):
                        self.insert_bss(1, today, status)
                        self.insert_bss(2, today, status)
                        today += timedelta(days=1)
        else:
            pass

    def get_week(self):
        today = date.today()
        if today.weekday() == 4:
            last_friday = today
        else:
            days_to_last_friday = (today.weekday() - 4) % 7
            last_friday = today - timedelta(days=days_to_last_friday)

        days_to_next_thursday = (3 - today.weekday() + 7) % 7
        next_thursday = today + timedelta(days=days_to_next_thursday)

        return [last_friday, next_thursday]

    def get_check_week(self, friday):
        date_friday = datetime.strptime(friday, "%Y-%m-%d")
        next_thursday = date_friday + timedelta(days=6)
        str_thursdary = next_thursday.strftime("%Y-%m-%d")
        return [friday, str_thursdary]

    def insert_pltd(self, unit, tanggal, status):
        query = f"INSERT INTO rompltd (unit, tanggal, status) VALUES (%s, %s, %s)"
        value = [unit, tanggal, status]
        connection(query, "insert", value)

    def insert_pv(self, unit, tanggal, status):
        query = f"INSERT INTO rompv (unit, tanggal, status) VALUES (%s, %s, %s)"
        value = [unit, tanggal, status]
        connection(query, "insert", value)

    def insert_bss(self, unit, tanggal, status):
        query = f"INSERT INTO rombss (unit, tanggal, status) VALUES (%s, %s, %s)"
        value = [unit, tanggal, status]
        connection(query, "insert", value)

    def get_pltd(self, tanggal):
        query = f"SELECT * FROM rompltd WHERE tanggal = %s"
        value = [tanggal]
        result = connection(query, "select", value)
        return result

    def get_pv(self, tanggal):
        query = f"SELECT * FROM rompv WHERE tanggal = %s"
        value = [tanggal]
        result = connection(query, "select", value)
        return result

    def get_bss(self, tanggal):
        query = f"SELECT * FROM rombss WHERE tanggal = %s"
        value = [tanggal]
        result = connection(query, "select", value)
        return result

    def get_pltd_week(self):
        query = f"SELECT * FROM rompltd WHERE tanggal >= %s AND tanggal <= %s"
        value = self.get_week()
        result = connection(query, "select", value)
        return result

    def get_pv_week(self):
        query = f"SELECT * FROM rompv WHERE tanggal >= %s AND tanggal <= %s"
        value = self.get_week()
        result = connection(query, "select", value)
        return result

    def get_bss_week(self):
        query = f"SELECT * FROM rombss WHERE tanggal >= %s AND tanggal <= %s"
        value = self.get_week()
        result = connection(query, "select", value)
        return result

    def get_data_week(self, unit, friday):
        query = f"SELECT tanggal FROM {unit} WHERE tanggal >= %s AND tanggal <= %s"
        value = self.get_check_week(friday)
        result = connection(query, "select", value)
        return result

    def get_data_month(self, bulan, unit):
        query = f"SELECT unit, tanggal, status FROM {unit} WHERE DATE_FORMAT(tanggal, '%Y-%m') = %s"
        value = [bulan]
        result = connection(query, "select", value)
        return result

    def delete_data_week(self, unit, friday):
        query = f"DELETE FROM {unit} WHERE tanggal >= %s AND tanggal <= %s"
        value = self.get_check_week(friday)
        connection(query, "delete", value)

    def check_rom(self, unit):
        today = datetime.now().strftime("%Y-%m-%d")
        query = f"SELECT * FROM {unit} WHERE tanggal = %s"
        value = [today]
        result = connection(query, "select", value)
        return result
