# This manifest is to make sure a package is installed

$pkg_name = 'flask'

package {$pkg_name:
    ensure   => '2.1.0',
    provider => 'pip3'
}