#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
import cv2;

ruta = '/home/napoleon/codigo/curso_opencv/imagenes/tux.jpg';
imagen = cv2.imread(ruta);
ruta_copia = '/home/napoleon/codigo/curso_opencv/imagenes/tux_copia.jpg';
cv2.imwrite(ruta_copia,imagen);
imagen_copia = cv2.imread(ruta_copia)
cv2.imshow('Original', imagen)
cv2.imshow('Copia', imagen_copia)
cv2.waitKey(0)
cv2.destroyAllWindows()