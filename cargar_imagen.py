import cv2;

ruta = '/home/napoleon/codigo/curso_opencv/imagenes/tux.jpg';
imagen = cv2.imread(ruta);
cv2.imshow('Copy', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()