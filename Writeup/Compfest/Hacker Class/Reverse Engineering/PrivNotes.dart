package:meta/meta.dart
Wfile:///C:/src/flutter/.pub-cache/hosted/pub.dartlang.org/meta-1.7.0/lib/meta_meta.dart
// Copyright (c) 2020, the Dart project authors. Please see the AUTHORS file
// for details. All rights reserved. Use of this source code is governed by a
// BSD-style license that can be found in the LICENSE file.
/// Annotations that describe the intended use of other annotations.
library meta_meta;
/// An annotation used on classes that are intended to be used as annotations
/// to indicate the kinds of declarations and directives for which the
/// annotation is appropriate.
/// The kinds are represented by the constants defined in [TargetKind].
/// Tools, such as the analyzer, can provide feedback if
/// * the annotation is associated with anything other than a class, where the
///   class must be usable as an annotation (that is, contain at least one
///   `const` constructor).
/// * the annotated annotation is associated with anything other than the kinds
///   of declarations listed as valid targets.
@Target({TargetKind.classType})
class Target {
  /// The kinds of declarations with which the annotated annotation can be
  /// associated.
  final Set<TargetKind> kinds;
  const Target(this.kinds);
/// An enumeration of the kinds of targets to which an annotation can be
/// applied.
enum TargetKind {
  /// Indicates that an annotation is valid on any class declaration.
  classType,
  /// Indicates that an annotation is valid on any enum declaration.
  enumType,
  /// Indicates that an annotation is valid on any extension declaration.
  extension,
  /// Indicates that an annotation is valid on any field declaration, both
  /// instance and static fields, whether it's in a class, mixin or extension.
  field,
  /// Indicates that an annotation is valid on any top-level function
  /// declaration.
  function,
  /// Indicates that an annotation is valid on the first directive in a library,
  /// whether that's a `library`, `import`, `export` or `part` directive. This
  /// doesn't include the `part of` directive in a part file.
  library,
  /// Indicates that an annotation is valid on any getter declaration, both
  /// instance or static getters, whether it's in a class, mixin, extension, or
  /// at the top-level of a library.
  getter,
  /// Indicates that an annotation is valid on any method declaration, both
  /// instance and static methods, whether it's in a class, mixin or extension.
  method,
  /// Indicates that an annotation is valid on any mixin declaration.
  mixinType,
  /// Indicates that an annotation is valid on any formal parameter declaration,
  /// whether it's in a function, method, constructor, or closure.
  parameter,
  /// Indicates that an annotation is valid on any setter declaration, both
  /// instance or static setters, whether it's in a class, mixin, extension, or
  /// at the top-level of a library.
  setter,
  /// Indicates that an annotation is valid on any top-level variable
  /// declaration.
  topLevelVariable,
  /// Indicates that an annotation is valid on any declaration that introduces a
  /// type. This includes classes, enums, mixins and typedefs, but does not
  /// include extensions because extensions don't introduce a type.
  type,
  /// Indicates that an annotation is valid on any typedef declaration.
  typedefType,
extension TargetKindExtension on TargetKind {
  /// Return a user visible string used to describe this target kind.
  String get displayString {
    switch (this) {
      case TargetKind.classType:
        return 'classes';
      case TargetKind.enumType:
        return 'enums';
      case TargetKind.extension:
        return 'extensions';
      case TargetKind.field:
        return 'fields';
      case TargetKind.function:
        return 'top-level functions';
      case TargetKind.library:
        return 'libraries';
      case TargetKind.getter:
        return 'getters';
      case TargetKind.method:
        return 'methods';
      case TargetKind.mixinType:
        return 'mixins';
      case TargetKind.parameter:
        return 'parameters';
      case TargetKind.setter:
        return 'setters';
      case TargetKind.topLevelVariable:
        return 'top-level variables';
      case TargetKind.type:
        return 'types (classes, enums, mixins, or typedefs)';
      case TargetKind.typedefType:
        return 'typedefs';
    }
package:meta/meta_meta.dart
<file:///C:/Users/ACER/StudioProjects/privnotes/lib/main.dart
:import 'package:flutter/material.dart';
void main() {
  runApp(const izoRPQJVfq());
class izoRPQJVfq extends StatelessWidget {
  const izoRPQJVfq({Key? key}) : super(key: key);
  static const xenUplybkt = 'PrivNotes';
  @override
  Widget build(BuildContext pnvcpdPYOC) {
    return MaterialApp(
      title: xenUplybkt,
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: const Text(xenUplybkt),
        ),
        body: UhcEpFGBRM(),
      ),
    );
class UhcEpFGBRM extends StatelessWidget {
  UhcEpFGBRM({Key? key}) : super(key: key);
  final TYfdNLewmB = TextEditingController();
  bool aVPRtlcZip(String ZbalwJOEHB) {
    var EjUAATbIos = false;
    var HnkCQqPbEL = [92, 14, 81, 92, 75, 69, 94, 13, 101, 57, 97, 47, 107, 12, 62, 59, 84, 124, 37, 33, 112, 19, 117, 40, 35, 116, 120, 28, 117, 54, 125, 38, 82, 33, 105, 51, 84, 95, 104, 116, 32, 109, 65, 26, 106, 101, 42, 68, 91, 54, 37, 61, 100, 57, 55, 50, 40, 53, 113, 51, 59, 75, 125, 63, 20, 36, 71, 84, 59, 24, 28, 82, 31, 49, 109, 74, 16, 46, 88, 114, 119, 110, 51, 65, 113, 49, 67, 48, 124, 120, 80, 119, 30, 94, 17, 116, 124, 44, 101, 30, 113, 83, 70, 79, 122, 55, 101, 120, 103, 64, 86, 73, 70, 53, 48, 107, 46, 49, 99, 29, 117, 43, 58, 105, 54, 119, 25, 14, 68, 107, 14, 121, 62, 86, 17, 18, 33, 12, 56, 62, 50, 36, 32, 69, 110, 18, 29, 12, 34, 72, 61, 23, 24, 43, 101, 94, 52, 51, 107, 60, 106, 77, 49, 15, 78, 97, 39, 59, 96, 72, 24, 82, 69];
    for(var i = 0; i < ZbalwJOEHB.length; i++) {
      if(ZbalwJOEHB.codeUnitAt(i) ^ OaqqprViEU.eXyyDPIZKn[0].codeUnitAt(i) ^ OaqqprViEU.eXyyDPIZKn[1].codeUnitAt(i) != HnkCQqPbEL[i]) {
        break;
      }
      if(ZbalwJOEHB.codeUnitAt(i) == 125 && i == ZbalwJOEHB.length - 1) {
        EjUAATbIos = true;
        break;
      }
    }
    return EjUAATbIos;
  }
  @override
  Widget build(BuildContext pnvcpdPYOC) {
    return Center(
        child: Column(
          children: <Widget>[
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 16),
              child: TextFormField(
                controller: TYfdNLewmB,
                decoration: const InputDecoration(
                  border: UnderlineInputBorder(),
                  labelText: 'Enter the pass code!',
                  icon: Padding(
                    padding: EdgeInsets.only(top: 15.0),
                    child: Icon(Icons.lock),
                  ),
                ),
                obscureText: true,
              ),
            ),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 4, vertical: 4),
              child: ElevatedButton(
                onPressed: () {
                  if(aVPRtlcZip(TYfdNLewmB.text)) {
                    Navigator.push(
                      pnvcpdPYOC,
                      MaterialPageRoute(builder: (pnvcpdPYOC) => const OaqqprViEU()),
                    );
                  }
                },
                child: const Text('View Notes'),
              ),
            ),
          ],
        )
    );
  }
  }
class OaqqprViEU extends StatelessWidget {
  const OaqqprViEU({Key? key}) : super(key: key);
  static final eXyyDPIZKn = ["I really like pineapples on pizza.... Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed suscipit libero ac felis commodo vulputate. Suspendisse risus sapien, accumsan quis dictum sed, hendrerit quis sem.",
    "Vanilla tastes better than chocolate. Praesent sit amet blandit sapien. Duis hendrerit blandit magna sit amet blandit. Curabitur vulputate, quam a posuere euismod, leo erat malesuada nunc, at euismod massa neque nec sem."];
  @override
  Widget build(BuildContext pnvcpdPYOC) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Super Secret Notes'),
      ),
      body: Center(
        child: Column(
          children: <Widget>[
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
              child: Card(
                child: SizedBox(
                  height: 75,
                  child: Center(child: Text(eXyyDPIZKn[0])),
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
              child: Card(
                child: SizedBox(
                  height: 75,
                  child: Center(child: Text(eXyyDPIZKn[1])),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}