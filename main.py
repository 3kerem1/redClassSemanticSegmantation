import cv2
import numpy as np

# Kamera nesnesi oluştur
cap = cv2.VideoCapture(0)  # 0, varsayılan kamera

while True:
    # Kamera görüntüsünü al
    ret, frame = cap.read()

    if not ret:
        print("Kamera görüntüsü alınamadı. Lütfen kameranızı kontrol edin.")
        break

    # Görüntüyü HSV renk uzayına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı renk için alt ve üst sınırları belirle
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    # Kırmızı renk için bir başka aralık
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    # Her iki maskeyi birleştir
    mask = mask1 + mask2

    # Maskeyi orijinal görüntü ile birleştir
    red_detection = cv2.bitwise_and(frame, frame, mask=mask)

    # Sonuçları göster
    cv2.imshow('Original Image', frame)
    cv2.imshow('Detected Red Color', red_detection)

    # Çıkmak için 'q' tuşuna basılmasını kontrol et
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
