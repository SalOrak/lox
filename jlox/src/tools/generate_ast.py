import sys

# Default
output_dir="/home/hector/personal/lox/jlox/src/com/jlox/Lox/"

if len(sys.argv) == 2:
    output_dir = sys.argv[1]

def defineVisitor(file, base_name, types):
    file.write("  interface Visitor<R>{\n")
    for type in types:
        type_name = type.split(":")[0].strip()
        file.write("    R visit" + type_name + base_name + "(" + type_name + " " + base_name.lower() + ");\n")
    file.write("  }\n")

def defineType(file, base_name, class_name, field_list):
    file.write("  static class " + class_name + " extends " + base_name  + " {\n")

    # Constructor
    file.write("    " + class_name + "(" + field_list + ") {\n")

    # Store parameters in fields
    fields = field_list.split(", ")
    for field in fields:
        name = field.split(" ")[1]
        file.write("      this." + name + " = " + name + ";\n")
    file.write("    }\n")

    # Visitor pattern
    file.write("\n")
    file.write("    @Override\n")
    file.write("    <R> R accept(Visitor<R> visitor) {\n")
    file.write("      return visitor.visit" + class_name + base_name + "(this);\n")
    file.write("    }\n")
    
    # Fields
    file.write("\n")
    for field in fields:
        file.write("    final " + field + ";\n")

    file.write("  }\n")

def defineAst(outdir, base_name, types):
    path = outdir + "/" + base_name + ".java"
    
    with  open(path, 'w') as file:
        file.write("package com.jlox.Lox;\n\n")
        file.write("import java.util.List;\n\n")
        file.write("abstract class " + base_name + "{\n\n")
        defineVisitor(file, base_name, types)
        for type in types:
            class_name = type.split(":")[0].strip()
            fields = type.split(":")[1].strip()
            defineType(file, base_name, class_name, fields)

        file.write("\n")
        file.write("  abstract <R> R accept(Visitor<R> visitor);\n")
        file.write("}\n\n")
        
defineAst(output_dir, "Expr", [
    "Binary   : Expr left, Token operator, Expr right",
    "Grouping : Expr expression",
    "Literal  : Object value",
    "Unary    : Token operator, Expr right"
])
