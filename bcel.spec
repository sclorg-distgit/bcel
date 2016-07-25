%global pkg_name bcel
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        5.2
Release:        18.6%{?dist}
Epoch:          0
Summary:        Byte Code Engineering Library
License:        ASL 2.0
URL:            http://commons.apache.org/proper/commons-bcel/
Source0:        http://archive.apache.org/dist/commons/bcel/source/bcel-5.2-src.tar.gz
# Upstream uses Maven 1, which is not available in Fedora.
# The following is upstream project.xml converted to Maven 2/3.
Source1:        %{pkg_name}-pom.xml
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(regexp:regexp)
BuildRequires:  %{?scl_prefix}mvn(org.apache.felix:maven-bundle-plugin)

%description
The Byte Code Engineering Library (formerly known as JavaClass) is
intended to give users a convenient possibility to analyze, create, and
manipulate (binary) Java class files (those ending with .class). Classes
are represented by objects which contain all the symbolic information of
the given class: methods, fields and byte code instructions, in
particular.  Such objects can be read from an existing file, be
transformed by a program (e.g. a class loader at run-time) and dumped to
a file again. An even more interesting application is the creation of
classes from scratch at run-time. The Byte Code Engineering Library
(BCEL) may be also useful if you want to learn about the Java Virtual
Machine (JVM) and the format of Java .class files.  BCEL is already
being used successfully in several projects such as compilers,
optimizers, obsfuscators and analysis tools, the most popular probably
being the Xalan XSLT processor at Apache.

%package javadoc
Summary:        API documentation for %{pkg_name}

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
cp -p %{SOURCE1} pom.xml
%mvn_alias : bcel:
%mvn_file : %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc README.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:5.2-18.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:5.2-18.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:5.2-18.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:5.2-18.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:5.2-18.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:5.2-18.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 05.2-18
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:5.2-17
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Fri Jun 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:5.2-16
- Complete spec file rewrite
- Build with Maven instead of Ant
- Remove manual subpackage

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:5.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Tom Callaway <spot@fedoraproject.org> - 0:5.2-14
- Package NOTICE.txt

* Tue Aug 21 2012 Andy Grimm <agrimm@gmail.com> - 0:5.2-13
- This package should not own _mavendepmapfragdir (RHBZ#850005)
- Build with maven, and clean up deprecated spec constructs
- Fix pom file (See http://jira.codehaus.org/browse/MEV-592)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 24 2012 Gerard Ryan <galileo@fedoraproject.org> - 0:5.2-11
- Inject OSGI Manifest.

* Wed Jan 11 2012 Ville Skyttä <ville.skytta@iki.fi> - 0:5.2-10
- Specify explicit source encoding to fix build with Java 7.
- Install jar and javadocs unversioned.
- Crosslink with JDK javadocs.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 13 2010 Alexander Kurtakov <akurtako@redhat.com> 0:5.2-8
- Use global.
- Drop gcj_support.
- Fix groups.
- Fix build.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:5.2-7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:5.2-6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 04 2008 Permaine Cheung <pcheung at redhat.com> 0:5.2-5.1
- Do not install poms in /usr/share/maven2/default_poms

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:5.2-5
- drop repotag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:5.2-4jpp.2
- Autorebuild for GCC 4.3

* Tue Jan 22 2008 Permaine Cheung <pcheung at redhat.com> 0:5.2-3jpp.1
- Merge with upstream

* Mon Jan 07 2008 Permaine Cheung <pcheung at redhat.com> 0:5.2-2jpp.2
- Fixed unowned directory (Bugzilla 246185)

* Fri Nov 16 2007 Ralph Apel <r.apel@r-apel.de> 0:5.2-3jpp
- Install poms unconditionally
- Add pom in ./maven2/default_poms
- Add org.apache.bcel:bcel depmap frag

* Wed Sep 19 2007 Permaine Cheung <pcheung at redhat.com> 0:5.2-2jpp.1
- Update to 5.2 in Fedora

* Mon Sep  4 2007 Jason Corley <jason.corley@gmail.com> 0:5.2-2jpp
- use official 5.2 release tarballs and location
- change vendor and distribution to macros
- add missing requires on and maven-plugin-test, maven-plugins-base, and
  maven-plugin-xdoc 
- macro bracket fixes
- remove demo subpackage (examples are not included in the distribution tarball)
- build in mock

* Wed Jun 27 2007 Ralph Apel <r.apel@r-apel.de> 0:5.2-1jpp
- Upgrade to 5.2
- Drop bootstrap option: not necessary any more
- Add pom and depmap frags

* Fri Feb 09 2007 Ralph Apel <r.apel@r-apel.de> 0:5.1-10jpp
- Fix empty-%%post and empty-%%postun
- Fix no-cleaning-of-buildroot

* Fri Feb 09 2007 Ralph Apel <r.apel@r-apel.de> 0:5.1-9jpp
- Optionally build without maven
- Add bootstrap option

* Thu Aug 10 2006 Matt Wringe <mwringe at redhat.com> 0:5.1-8jpp
- Add missing requires for Javadoc task

* Sun Jul 23 2006 Matt Wringe <mwringe at redhat.com> 0:5.1-7jpp
- Add conditional native compilation
- Change spec file encoding from ISO-8859-1 to UTF-8
- Add missing BR werken.xpath and ant-apache-regexp

* Tue Apr 11 2006 Ralph Apel <r.apel@r-apel.de> 0:5.1-6jpp
- First JPP-1.7 release
- Use tidyed sources from svn
- Add resources to build the manual
- Add examples to -demo subpackage
- Build with maven by default
- Add option to build with straight ant

* Fri Nov 19 2004 David Walluck <david@jpackage.org> 0:5.1-5jpp
- rebuild to fix packager

* Sat Nov 06 2004 David Walluck <david@jpackage.org> 0:5.1-4jpp
- rebuild with javac 1.4.2

* Sat Oct 16 2004 David Walluck <david@jpackage.org> 0:5.1-3jpp
- rebuild for JPackage 1.6

* Fri Aug 20 2004 Ralph Apel <r.apel at r-apel.de> 0:5.1-2jpp
- Build with ant-1.6.2

* Sun May 11 2003 David Walluck <david@anti-microsoft.org> 0:5.1-1jpp
- 5.1
- update for JPackage 1.5

* Mon Mar 24 2003 Nicolas Mailhot <Nicolas.Mailhot (at) JPackage.org> - 5.0-6jpp
- For jpackage-utils 1.5

* Tue Feb 25 2003 Ville Skyttä <ville.skytta@iki.fi> - 5.0-5jpp
- Rebuild to get docdir right on modern distros.
- Fix License tag and source file perms.
- Built with IBM's 1.3.1SR3 (doesn't build with Sun's 1.4.1_01).

* Tue Jun 11 2002 Henri Gomez <hgomez@slib.fr> 5.0-4jpp
- use sed instead of bash 2.x extension in link area to make spec compatible
  with distro using bash 1.1x

* Tue May 07 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 5.0-3jpp 
- vendor, distribution, group tags

* Wed Jan 23 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 5.0-2jpp 
- section macro
- no dependencies for manual and javadoc package

* Tue Jan 22 2002 Henri Gomez <hgomez@slib.fr> 5.0-1jpp
- bcel is now a jakarta apache project
- dependency on jakarta-regexp instead of gnu.regexp 
- created manual package

* Sat Dec 8 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 4.4.1-2jpp
- javadoc into javadoc package
- Requires: and BuildRequires: gnu.regexp

* Wed Nov 21 2001 Christian Zoffoli <czoffoli@littlepenguin.org> 4.4.1-1jpp
- removed packager tag
- new jpp extension
- 4.4.1

* Thu Oct 11 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 4.4.0-2jpp
- first unified release
- used lower case for name
- used original tarball
- s/jPackage/JPackage

* Mon Aug 27 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 4.4.0-1mdk
- first Mandrake release
