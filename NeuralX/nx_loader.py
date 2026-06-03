# nx_loader.py — Importador personalizado de NeuralX
# Permite que Python importe archivos .nx como módulos normales.
# Se debe llamar register() antes de cualquier import de librería .nx

import sys
import os
import importlib.abc
import importlib.machinery


class NeuralXFinder(importlib.abc.MetaPathFinder):
    """Encuentra módulos .nx en el path de búsqueda."""

    def find_spec(self, fullname, path, target=None):
        # Buscar en libs/ primero, luego en directorio actual
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        rutas_busqueda = [
            os.path.join(directorio_actual, 'libs'),  # buscar en libs/ primero
            directorio_actual,                          # luego en raíz
        ]
        if path:
            rutas_busqueda = list(path) + rutas_busqueda

        for entrada in rutas_busqueda:
            ruta_nx = os.path.join(entrada, fullname + ".nx")
            if os.path.isfile(ruta_nx):
                loader = NeuralXLoader(fullname, ruta_nx)
                return importlib.machinery.ModuleSpec(fullname, loader, origin=ruta_nx)
        return None


class NeuralXLoader(importlib.abc.Loader):
    """Carga y ejecuta archivos .nx como código Python."""

    def __init__(self, fullname, ruta):
        self.fullname = fullname
        self.ruta     = ruta

    def create_module(self, spec):
        return None   # usar el mecanismo por defecto

    def exec_module(self, module):
        module.__file__ = self.ruta
        module.__name__ = self.fullname
        # Agregar libs/ al path para que los .nx puedan importarse entre sí
        libs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'libs')
        if libs_path not in sys.path:
            sys.path.insert(0, libs_path)
        with open(self.ruta, "r", encoding="utf-8") as f:
            codigo = f.read()
        exec(compile(codigo, self.ruta, "exec"), module.__dict__)


def register():
    """Registra el importador .nx en el sistema de imports de Python."""
    # Agregar libs/ al path del sistema
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    libs_path = os.path.join(directorio_actual, 'libs')
    if libs_path not in sys.path:
        sys.path.insert(0, libs_path)

    for finder in sys.meta_path:
        if isinstance(finder, NeuralXFinder):
            return   # ya registrado
    sys.meta_path.insert(0, NeuralXFinder())
