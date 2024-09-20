-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Anamakine: localhost:8889
-- Üretim Zamanı: 29 Ara 2023, 15:15:01
-- Sunucu sürümü: 5.7.39
-- PHP Sürümü: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `giris`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kayit`
--

CREATE TABLE `kayit` (
  `kayit_id` int(11) NOT NULL,
  `ad` varchar(255) DEFAULT NULL,
  `soyad` varchar(255) DEFAULT NULL,
  `kullanici_adi` varchar(255) DEFAULT NULL,
  `sifre` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Tablo döküm verisi `kayit`
--

INSERT INTO `kayit` (`kayit_id`, `ad`, `soyad`, `kullanici_adi`, `sifre`) VALUES
(1, 'Seymen', 'Kayıkçı', 's3y0', '1234'),
(2, 'Seymen', 'Kayıkçı', 'navita', '123321'),
(3, 'ezgi', 'ayvaz', 'ezo', '123456'),
(4, 'burak', 'evrentug', 'brk123', '123456'),
(5, 'Burak', 'evrentug', 'brkev', '12345'),
(6, 'Mehmet Can', 'Dönmez', 'memo', '1234'),
(7, 'Şafak', 'Seven', 'Admin', '1234');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `pasaport`
--

CREATE TABLE `pasaport` (
  `pasaport_id` int(11) NOT NULL,
  `ad` varchar(255) DEFAULT NULL,
  `soyad` varchar(255) DEFAULT NULL,
  `tc` varchar(15) DEFAULT NULL,
  `dogum_tarihi` datetime DEFAULT NULL,
  `vize_turu` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Tablo döküm verisi `pasaport`
--

INSERT INTO `pasaport` (`pasaport_id`, `ad`, `soyad`, `tc`, `dogum_tarihi`, `vize_turu`) VALUES
(1, 'Aleyna', 'karpat', '60448122580', '2002-08-04 00:00:00', 'Öğrenci'),
(2, 'şehmus', 'akın', '123455654', '2023-12-26 00:00:00', 'Öğrenci'),
(3, 'Seymen ', 'kayıkçı', '50248712234', '2023-12-26 00:00:00', 'Öğrenci'),
(4, 'Şafak', 'Seven', '50248712234', '1982-05-05 00:00:00', 'Öğrenci');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `ucak_bileti`
--

CREATE TABLE `ucak_bileti` (
  `ucak_bileti_id` int(11) NOT NULL,
  `nereden` varchar(255) DEFAULT NULL,
  `nereye` varchar(255) DEFAULT NULL,
  `gidis_tarihi` datetime DEFAULT NULL,
  `donus_tarihi` datetime DEFAULT NULL,
  `yolcu_sayisi` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Tablo döküm verisi `ucak_bileti`
--

INSERT INTO `ucak_bileti` (`ucak_bileti_id`, `nereden`, `nereye`, `gidis_tarihi`, `donus_tarihi`, `yolcu_sayisi`) VALUES
(1, 'İzmir', 'Dubai', '2024-04-22 00:00:00', '2024-04-28 00:00:00', '2'),
(2, 'İzmir', 'Tokyo', '2024-04-22 00:00:00', '2024-05-22 00:00:00', '3'),
(3, 'Antalya', 'Tokyo', '2024-02-06 00:00:00', '2024-02-12 00:00:00', '9'),
(4, 'Ankara', 'Paris', '2023-12-26 00:00:00', '2024-02-01 00:00:00', '2'),
(5, 'İzmir', 'Dubai', '2023-12-26 00:00:00', '2023-12-26 00:00:00', '2'),
(6, 'İzmir', 'Tokyo', '2023-12-28 00:00:00', '2023-12-29 00:00:00', '3');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `vize`
--

CREATE TABLE `vize` (
  `vize_id` int(11) NOT NULL,
  `ad` varchar(255) DEFAULT NULL,
  `soyad` varchar(255) DEFAULT NULL,
  `dogum_tarihi` datetime DEFAULT NULL,
  `cinsiyet` varchar(255) DEFAULT NULL,
  `medeni_hal` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Tablo döküm verisi `vize`
--

INSERT INTO `vize` (`vize_id`, `ad`, `soyad`, `dogum_tarihi`, `cinsiyet`, `medeni_hal`) VALUES
(1, 'Seymen', 'Kayıkçı', '2002-02-22 00:00:00', 'Erkek', 'Bekar'),
(2, 'Ahmet', 'Durmaz', '2002-02-02 00:00:00', 'Erkek', 'Boşanmış'),
(3, 'Seymen', 'Kayıkçı', '2002-04-22 00:00:00', 'Erkek', 'Bekar'),
(4, 'mesut', 'ayanoğlu', '2001-02-01 00:00:00', 'Erkek', 'Boşanmış'),
(5, 'Ahmet', 'Durmaz', '2023-12-26 00:00:00', 'Erkek', 'Evli'),
(6, 'Seymen', 'Kayıkçı', '2002-04-22 00:00:00', 'Erkek', 'Boşanmış'),
(7, 'şafak', 'seven', '1982-05-05 00:00:00', 'Erkek', 'Evli');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `kayit`
--
ALTER TABLE `kayit`
  ADD PRIMARY KEY (`kayit_id`);

--
-- Tablo için indeksler `pasaport`
--
ALTER TABLE `pasaport`
  ADD PRIMARY KEY (`pasaport_id`);

--
-- Tablo için indeksler `ucak_bileti`
--
ALTER TABLE `ucak_bileti`
  ADD PRIMARY KEY (`ucak_bileti_id`);

--
-- Tablo için indeksler `vize`
--
ALTER TABLE `vize`
  ADD PRIMARY KEY (`vize_id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `kayit`
--
ALTER TABLE `kayit`
  MODIFY `kayit_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Tablo için AUTO_INCREMENT değeri `pasaport`
--
ALTER TABLE `pasaport`
  MODIFY `pasaport_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Tablo için AUTO_INCREMENT değeri `ucak_bileti`
--
ALTER TABLE `ucak_bileti`
  MODIFY `ucak_bileti_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Tablo için AUTO_INCREMENT değeri `vize`
--
ALTER TABLE `vize`
  MODIFY `vize_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
