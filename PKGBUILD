pkgname=python-onkyrimote
_pkgname=onkyrimote
pkgver=$(git describe --long --tags | sed 's/\([^-]*-\)g/r\1/;s/-/./g;s/^v//')
pkgrel=1
pkgdesc="Python library and command line utility for controlling Onkyo receivers through the RI protocol."
arch=('any')
url="https://github.com/kmohrf/onkyrimote"
license=('AGPLv3')
makedepends=('python-setuptools')
depends=('python')
optdepends=(
    'python-pigpio: support for Raspberry Pi'
)

package() {
    cd ..
    python setup.py install --root="${pkgdir}" --optimize=1
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
}
