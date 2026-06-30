-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.4.3 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.8.0.6908
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for contentplan
CREATE DATABASE IF NOT EXISTS `contentplan` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `contentplan`;

-- Dumping structure for table contentplan.analytics
CREATE TABLE IF NOT EXISTS `analytics` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content_id` int NOT NULL,
  `likes` int NOT NULL,
  `views` int NOT NULL,
  `shares` int NOT NULL,
  `timestamp` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `content_id` (`content_id`),
  CONSTRAINT `analytics_ibfk_1` FOREIGN KEY (`content_id`) REFERENCES `content` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table contentplan.analytics: ~19 rows (approximately)
INSERT INTO `analytics` (`id`, `content_id`, `likes`, `views`, `shares`, `timestamp`) VALUES
	(4, 2, 298, 4087, 142, '2026-06-26 09:37:38'),
	(5, 3, 1928, 11722, 433, '2026-06-26 09:37:38'),
	(6, 4, 1182, 18764, 506, '2026-06-26 09:37:38'),
	(7, 5, 3535, 3159, 26, '2026-06-26 09:37:38'),
	(8, 6, 6231, 55602, 334, '2026-06-26 09:37:38'),
	(9, 7, 2376, 20955, 93, '2026-06-26 09:37:38'),
	(10, 8, 7672, 22392, 256, '2026-06-26 09:37:38'),
	(11, 9, 13215, 54365, 707, '2026-06-26 09:37:38'),
	(12, 10, 607, 16849, 565, '2026-06-26 09:37:38'),
	(13, 11, 1710, 7089, 461, '2026-06-26 09:37:38'),
	(14, 12, 7631, 50923, 182, '2026-06-26 09:37:38'),
	(15, 13, 4098, 18848, 496, '2026-06-26 09:37:38'),
	(16, 14, 12078, 93464, 205, '2026-06-26 09:37:38'),
	(17, 15, 13461, 28550, 708, '2026-06-26 09:37:38'),
	(18, 16, 529, 18014, 573, '2026-06-26 09:37:38'),
	(19, 17, 4885, 38224, 443, '2026-06-26 09:37:38'),
	(20, 18, 6465, 86330, 385, '2026-06-26 09:37:38'),
	(21, 19, 2411, 20877, 57, '2026-06-26 09:37:38'),
	(22, 20, 564, 7247, 681, '2026-06-26 09:37:38');

-- Dumping structure for table contentplan.content
CREATE TABLE IF NOT EXISTS `content` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `caption` text NOT NULL,
  `media_url` varchar(500) DEFAULT NULL,
  `platform` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `user_id` int NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `content_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table contentplan.content: ~19 rows (approximately)
INSERT INTO `content` (`id`, `title`, `caption`, `media_url`, `platform`, `status`, `user_id`, `created_at`, `updated_at`) VALUES
	(2, 'Paket Haji Mujamalah - Tanpa Antri', '🕋✨ Wujudkan impian berhaji lebih cepat tanpa menunggu puluhan tahun.\r\n\r\n✅ Visa Mujamalah resmi\r\n✅ 100% uang kembali jika visa tidak terbit\r\n✅ Hotel Mekkah & Madinah bintang 3\r\n✅ Armuna Maktab G 8 hari\r\n✅ Program 26 hari\r\n✅ Flight Qatar / Etihad\r\n\r\n💼 Dibimbing muthawwif berpengalaman\r\n🍽️ Konsumsi 3x sehari menu Indonesia\r\n🚌 Transportasi terbaru & nyaman\r\n📆 Keberangkatan: 13 Mei – 7 Juni 2026\r\n💰 Start from: 19.500 USD\r\n\r\n_____\r\n\r\n📍 Alamat Kantor: Gedung Buncit 36, Jl. Warung Jati Barat No.36, RT.2/RW.11, Ragunan, Ps. Minggu, Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12550\r\n_____\r\n\r\n📢Info lengkap:\r\n☎ 0852-1111-0505 (WA)\r\n\r\n#umrohjakarta #hajifuroda\r\n#hajimujamalah #umrohjakarta #umrohmurah', 'static/uploads/WhatsApp_Image_2026-06-13_at_15.11.08.jpeg', 'instagram', 'posted', 1, '2026-06-13 08:12:28', '2026-06-23 06:21:37'),
	(3, '14 Hari Menuju Ramadhan', '14 hari menuju Ramadhan.\r\nSaatnya evaluasi diri dan perbaiki niat 🌙✨\r\n_____\r\n\r\n📍 Alamat Kantor: Gedung Buncit 36, Jl. Warung Jati Barat No.36, RT.2/RW.11, Ragunan, Ps. Minggu, Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12550\r\n_____\r\n\r\n📢Info lengkap:\r\n☎ 0852-1111-0505 (WA)\r\n\r\n#Umrah2026 #HajiUmrah #Daytamasw #TravelUmrahResmi #SahabatIbadahmu UmrahMudah', 'static/uploads/Screenshot_2026-06-13_151732.png', 'instagram', 'scheduled', 1, '2026-06-13 08:20:45', '2026-06-13 08:20:45'),
	(4, '6 Hari Menuju Ramadhan', '🌙 6 Hari Menuju Ramadhan 🤲✨\r\n\r\nAllah berfirman:\r\n\r\n“Bulan Ramadan adalah bulan yang di dalamnya diturunkan Al-Qur’an sebagai petunjuk bagi manusia.”\r\n(QS. Al-Baqarah: 185)\r\n\r\nMari persiapkan hati, iman, dan amal terbaik untuk menyambut bulan penuh berkah 🤲✨\r\nSemoga kita dipertemukan dengan Ramadhan tahun ini.\r\n\r\n#Ramadhan2026 #MenujuRamadhan #RamadhanMubarak #BulanBerkah', 'static/uploads/Screenshot_2026-06-13_152248.png', 'instagram', 'scheduled', 1, '2026-06-13 08:23:03', '2026-06-13 08:23:03'),
	(5, 'Ramadhan', 'Marhaban ya Ramadan 1447 H 🌙✨\r\n\r\nBulan penuh berkah telah tiba… saatnya membersihkan hati, memperbanyak ibadah, dan mendekatkan diri kepada Allah SWT 🤲\r\n\r\nSemoga Ramadan kali ini membawa ketenangan, keberkahan, dan kesempatan untuk menjadi pribadi yang lebih baik 💛\r\n\r\nSelamat menunaikan ibadah puasa 🙏\r\nSemoga setiap langkah kita menuju ridha-Nya.\r\n\r\n#MarhabanYaRamadan #Ramadan1447H #RamadanMubarak #BulanBerkah #DaytamaSinergiWisata', 'static/uploads/Screenshot_2026-06-13_152357.png', 'instagram', 'scheduled', 1, '2026-06-13 08:24:23', '2026-06-13 08:26:20'),
	(6, 'GRWM Pendaftaran di Daytama', 'Bismillah… Langkah menuju Baitullah dimulai dari sini 🤍\r\n\r\nDaftar Umroh di Daytama, proses jelas , aman dan terpercaya. ✨\r\n_____\r\n\r\n📍 Alamat Kantor: Gedung Buncit 36, Jl. Warung Jati Barat No.36, RT.2/RW.11, Ragunan, Ps. Minggu, Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12550\r\n_____\r\n\r\n📢Info lengkap:\r\n☎ 0852-1111-0505 (WA)\r\n#umroh #travelumroh #umrohterpercaya #umroh2026 #hajiplus #haji', NULL, 'tiktok', 'draft', 1, '2026-06-13 08:25:35', '2026-06-13 08:25:35'),
	(7, '3 Restoran Favorit di Arab Saudi', '🍽️ Umroh makin lengkap kalau cobain 3 restoran favorit ini di Arab Saudi 🇸🇦✨\r\n_____\r\n\r\n📍 Alamat Kantor: Gedung Buncit 36, Jl. Warung Jati Barat No.36, RT.2/RW.11, Ragunan, Ps. Minggu, Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12550\r\n_____\r\n\r\n📢Info lengkap:\r\n☎ 0852-1111-0505 (WA)\r\n\r\n#Umrah2026 #HajiUmrah #travelterdekat #TravelUmrahResmi #hajiplus', 'static/uploads/Screenshot_2026-06-13_152730.png', 'instagram', 'posted', 1, '2026-06-13 08:28:47', '2026-06-25 13:33:41'),
	(8, '3 Mitos Umroh', '✨Yuk cari tahu faktanya supaya ibadah makin tenang dan maksimal 🕋✨\r\n_____\r\n\r\n📍 Alamat Kantor: Gedung Buncit 36, Jl. Warung Jati Barat No.36, RT.2/RW.11, Ragunan, Ps. Minggu, Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12550\r\n_____\r\n\r\n📢Info lengkap:\r\n☎ 0852-1111-0505 (WA)\r\n\r\n#Umrah2026 #HajiUmrah #umroh #TravelUmrahResmi #hajivvip', 'static/uploads/Screenshot_2026-06-13_153113.png', 'tiktok', 'scheduled', 1, '2026-06-13 08:31:35', '2026-06-13 08:31:35'),
	(9, 'Nikah Dulu atau Umroh Dulu?', 'Nikah dulu 💍 atau Umroh dulu 🕋 — kalau kamu dikasih pilihan, pilih yang mana?\r\n\r\n___\r\n\r\n📍 Alamat Kantor: Gedung Buncit 36, Jl. Warung Jati Barat No.36, RT.2/RW.11, Ragunan, Ps. Minggu, Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12550\r\n___\r\n\r\n📢Info lengkap:\r\n☎ 0852-1111-0505 (WA)\r\n\r\n#Umrah2026 #viral #genz #haji #travelumroh', 'static/uploads/Screenshot_2026-06-13_153256.png', 'tiktok', 'posted', 1, '2026-06-13 08:33:29', '2026-06-26 09:30:16'),
	(10, 'Syarat Daftar Haji 2026', '🕋 Siap berangkat ke Baitullah tahun 2026?\r\n\r\nPastikan dokumen Anda sudah lengkap agar proses pendaftaran haji berjalan lancar dan tanpa kendala ✨\r\n_____\r\n\r\n📍 Alamat Kantor: Gedung Buncit 36, Jl. Warung Jati Barat No.36, RT.2/RW.11, Ragunan, Ps. Minggu, Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12550\r\n_____\r\n\r\n📢Info lengkap:\r\n☎ 0852-1111-0505 (WA)\r\n\r\n#haji #RamadanMubarak #umroh #umroh2026 #i̇slam', 'static/uploads/Screenshot_2026-06-13_153410.png', 'instagram', 'scheduled', 1, '2026-06-13 08:35:17', '2026-06-13 08:35:17'),
	(11, 'Solusi Haji Tanpa Antri', '✨ Solusi Haji Tanpa Antri ✨\r\n\r\nWujudkan impian berangkat ke Tanah Suci dengan program terbaik, fasilitas nyaman, dan pelayanan maksimal 🕋\r\n\r\n✔️ Pilihan paket 14 & 24 hari\r\n✔️ Hotel Mekkah & Madinah pilihan\r\n✔️ Maskapai internasional\r\n✔️ Makan 3x sehari\r\n✔️ Pembimbing & muthawif berpengalaman\r\n✔️ Perlengkapan eksklusif\r\n✔️ Dan masih banyak program lainnya yang bisa disesuaikan dengan kebutuhan Anda.\r\n\r\n_________________________________________\r\n\r\n📌 Kuota terbatas!\r\nYuk konsultasi & pilih program terbaik Anda sekarang.\r\n\r\n📲 Info & booking: 0852-1111-0505\r\n#HajiTanpaAntri #Haji2026 #hajifuroda #hajivvip', 'static/uploads/Screenshot_2026-06-13_153622.png', 'instagram', 'scheduled', 1, '2026-06-13 08:36:51', '2026-06-13 08:36:51'),
	(12, '3 Fakta Haji Indonesia', 'Tahukah kamu? 🤔\r\nIni 3 fakta Haji Indonesia yang jarang dibahas! 🇮🇩🕋\r\n_____\r\n\r\n📍 Alamat Kantor: Gedung Buncit 36, Jl. Warung Jati Barat No.36, RT.2/RW.11, Ragunan, Ps. Minggu, Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12550\r\n_____\r\n\r\n📢Info lengkap:\r\n☎ 0852-1111-0505 (WA)\r\n\r\n#viral #umroh #haji #umrohmurah', 'static/uploads/Screenshot_2026-06-13_153720.png', 'tiktok', 'scheduled', 1, '2026-06-13 08:38:21', '2026-06-13 08:38:21'),
	(13, 'Lokasi Penting di Masjid Nabawi', 'Tips umroh nih! ✨\r\nLokasi penting di Masjid Nabawi yang perlu jamaah tahu 🕌📍\r\n\r\n_____\r\n\r\n📍 Alamat Kantor: Gedung Buncit 36, Jl. Warung Jati Barat No.36, RT.2/RW.11, Ragunan, Ps. Minggu, Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12550\r\n_____\r\n\r\n📢Info lengkap:\r\n☎ 0852-1111-0505 (WA)\r\n\r\n#hajifuroda #umroh2026 #umrohmurah #hajivvip #umrohhemat', 'static/uploads/Screenshot_2026-06-13_153854.png', 'instagram', 'scheduled', 1, '2026-06-13 08:40:06', '2026-06-13 08:40:06'),
	(14, 'Langkah kecil hari ini, lebih dekat ke Baitullah 🕋✨', 'Percuma nunggu… gak akan bawa kamu ke Tanah Suci 🤍\r\nLangkah kecil hari ini, lebih dekat ke Baitullah 🕋✨\r\n\r\n_____\r\n\r\n📍 Alamat Kantor: Gedung Buncit 36, Jl. Warung Jati Barat No.36, RT.2/RW.11, Ragunan, Ps. Minggu, Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12550\r\n_____\r\n\r\n📢Info lengkap:\r\n☎ 0852-1111-0505 (WA)\r\n\r\n#Umrah2026 #HajiUmrah #Daytamatravel #hajiplus i #hajif', 'static/uploads/Screenshot_2026-06-13_154033.png', 'tiktok', 'scheduled', 1, '2026-06-13 08:42:20', '2026-06-13 08:42:20'),
	(15, 'Yang Niat Haji Tahun Depan Wajib Liat Ini', '✨️Tabungan Haji Tanpa Ribet, Tanpa Antri, 100% Syariah !! ✨️\r\n\r\nHaji Mujamalah. Cukup DP $5,000 dan cicilan ringan, kamu bisa berangkat Haji 2026/2027.\r\n✅ Hotel dekat Masjidil Haram\r\n✅ Maskapai Garuda & Saudia\r\n🎁 Gratis emas 10 gram untuk kamu yang konsisten menabung. Bismillah, mulai langkahmu hari ini!\r\n\r\n📲 Yuk, daftarkan dirimu sekarang via link di bio atau WA ke 0852-1111-0505\r\n#Umroh2025 #UmrohBersama #UmrohImpian #DoaTerbaik #UmrohBersamaOrangTersayang #umroh #umrohmurah #umrohpromo #umroh2025 #umrohhemat #hajaraswad #daytama #umrohindonesia #umrohsunnah #sunnah #sunnahrasul #tipsumroh #travelumroh #infoumroh #UmrohBersamaDaytama #daytama\r\n#umrohmurah #umrohsesuaisunnah #tabunganhaji #menabung #cicilan #haji #hajimuamalah', 'static/uploads/Screenshot_2026-06-13_154329.png', 'tiktok', 'scheduled', 1, '2026-06-13 08:45:13', '2026-06-13 08:45:13'),
	(16, 'Idul fitri', 'Selamat Hari Raya Idulfitri 1447 H ✨\r\nSaatnya kembali ke fitrah, menyucikan hati, dan mempererat silaturahmi 🤍\r\n\r\nMohon maaf lahir dan batin 🙏\r\nSemoga setiap langkah kita dipenuhi keberkahan dan ketenangan 🌙', 'static/uploads/Screenshot_2026-06-13_154532.png', 'instagram', 'scheduled', 1, '2026-06-13 08:47:02', '2026-06-13 08:47:02'),
	(17, 'Umroh Ramadhan', '🌙 😱 UMROH RAMADHAN MULAI DARI 29 JUTAAN?! 😱\r\n\r\nBayangkan… shalat tarawih langsung di Masjidil Haram, sahur dan berbuka di Tanah Suci, dan itikaf di 10 malam terakhir Ramadan. 🕋✨\r\n\r\n___________\r\n\r\n📍 Alamat Kantor: Gedung Buncit 36, Jl. Warung Jati Barat No.36, RT.2/RW.11, Ragunan, Ps. Minggu, Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12550\r\n___________\r\n\r\n📢Info lengkap:\r\n☎ 0852-1111-0505 (WA)\r\n\r\n#Umrah2025 #HajiUmrah #Daytamasw #TravelUmrahResmi #SahabatIbadahmu #UmrahMudah #HajiDanUmrah #HajiMabrur #umroh #umrohmurah #umrohpromo #umroh2025 #umrohhemat #hajaraswad #daytama #umrohindonesia #umrohsunnah #sunnah #sunnahrasul #tipsumroh #travelumroh #infoumroh #UmrohBersamaDaytama #daytama', 'static/uploads/Screenshot_2026-06-13_154752.png', 'tiktok', 'scheduled', 1, '2026-06-13 08:48:51', '2026-06-13 08:48:51'),
	(18, 'QnA', 'Opsi pertanyaan yg akan ditanyakan : \r\n\r\nPembayaran pakai rupiah atau dollar ya?\r\n\r\n\r\nBerangkat tahun berapa kalau daftar sekarang?\r\n\r\n\r\nKak, harga paket hajinya fix atau bisa berubah?\r\n\r\n\r\nSekamar berapa orang?\r\n\r\n\r\nAda pembimbing selama di sana?\r\n\r\n\r\nTravelnya sudah berizin resmi?\r\n\r\n\r\nKantornya di mana?\r\n\r\n\r\nBisa datang langsung konsultasi?\r\n\r\n\r\nHaji Mujamalah itu apa bedanya dengan haji reguler?\r\n\r\n\r\nIni benar tanpa waiting list?', NULL, 'tiktok', 'draft', 1, '2026-06-13 08:51:19', '2026-06-13 08:51:19'),
	(19, 'timmy', 'apaya', NULL, 'instagram', 'posted', 1, '2026-06-16 09:17:39', '2026-06-16 09:18:06'),
	(20, 'cobain', 'coba', NULL, 'instagram', 'posted', 1, '2026-06-25 13:55:30', '2026-06-25 13:56:21');

-- Dumping structure for table contentplan.schedule
CREATE TABLE IF NOT EXISTS `schedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content_id` int NOT NULL,
  `scheduled_datetime` datetime NOT NULL,
  `posted_at` datetime DEFAULT NULL,
  `is_posted` tinyint(1) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_id` (`content_id`),
  CONSTRAINT `schedule_ibfk_1` FOREIGN KEY (`content_id`) REFERENCES `content` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table contentplan.schedule: ~17 rows (approximately)
INSERT INTO `schedule` (`id`, `content_id`, `scheduled_datetime`, `posted_at`, `is_posted`, `created_at`) VALUES
	(2, 2, '2026-06-20 19:00:00', '2026-06-23 13:21:29', 1, '2026-06-13 08:12:29'),
	(3, 3, '2027-01-26 21:00:00', NULL, 0, '2026-06-13 08:20:45'),
	(4, 4, '2027-02-03 19:00:00', NULL, 0, '2026-06-13 08:23:03'),
	(5, 5, '2027-02-08 08:00:00', NULL, 0, '2026-06-13 08:26:21'),
	(6, 7, '2026-06-24 12:00:00', '2026-06-25 20:33:41', 1, '2026-06-13 08:28:47'),
	(7, 8, '2026-06-28 21:00:00', NULL, 0, '2026-06-13 08:31:35'),
	(8, 9, '2026-06-26 09:00:00', '2026-06-26 16:30:16', 1, '2026-06-13 08:33:29'),
	(9, 10, '2026-06-27 19:00:00', NULL, 0, '2026-06-13 08:35:17'),
	(10, 11, '2026-06-28 17:00:00', NULL, 0, '2026-06-13 08:36:51'),
	(11, 12, '2026-07-03 08:00:00', NULL, 0, '2026-06-13 08:38:21'),
	(12, 13, '2026-06-28 09:00:00', NULL, 0, '2026-06-13 08:40:06'),
	(13, 14, '2026-07-14 08:00:00', NULL, 0, '2026-06-13 08:42:20'),
	(14, 15, '2026-12-31 21:00:00', NULL, 0, '2026-06-13 08:45:13'),
	(15, 16, '2027-03-10 07:00:00', NULL, 0, '2026-06-13 08:47:03'),
	(16, 17, '2027-01-01 12:00:00', NULL, 0, '2026-06-13 08:48:51'),
	(17, 19, '2026-06-16 16:18:00', '2026-06-16 16:18:06', 1, '2026-06-16 09:17:39'),
	(18, 20, '2026-06-25 20:56:00', '2026-06-25 20:56:21', 1, '2026-06-25 13:55:30');

-- Dumping structure for table contentplan.user
CREATE TABLE IF NOT EXISTS `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(80) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table contentplan.user: ~1 rows (approximately)
INSERT INTO `user` (`id`, `username`, `email`, `password_hash`, `created_at`) VALUES
	(1, 'admin', 'admin@daytama.com', 'scrypt:32768:8:1$I04D28Ks6YqEyAPW$a69646345cf74072243e771253dae0521bbc60783787e2a7d48c04dbba66bbabbd33147f3e72d19c9864928342aaa76240a54467e98d3b6bd22a3d9f3ca25834', '2026-06-13 03:56:53');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
