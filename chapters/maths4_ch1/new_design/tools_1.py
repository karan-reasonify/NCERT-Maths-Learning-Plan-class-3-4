# -*- coding: utf-8 -*-
"""Class 4, Chapter 1 "Shapes Around Us": the tool entries, one per approved tool, in the approved order (step 2, the tool
mapper). Only the structure fields are here: tool_id, title (EXACTLY the approved name), approved_no, ONE learning
objective, and the keys of content.VISUAL_KEY the tool draws; Tool 1 (the exploration tool) also has its 3 `notice`
prompts. Screen, controls, instruction, feedback, done_when and hints are for the brief writer (step 6).

The 22 tools are the pipeline's PROPOSAL, locked from tool_map.md (no content-team table existed for this chapter); see
CLASH 1 in content.py. The concept each tool serves and the book items proposed for it are in tool_map.locked.md.
"""
from __future__ import annotations

from topics_common import T  # noqa: F401

TOOLS = {
    # ---- Module 1: solid shapes (Tools 1 to 9)
    "blocks": T(
        "tool_blocks_for_buildings", "Blocks for Buildings", 1,
        "Students pick solid shapes for the roof, pillars and base of a building and compare the model with the real building.",
        notice=["Which blocks stand firm on the floor, and which ones roll?",
                "Which block could you use more than once?",
                "What changes when you swap one block for another?"],
        visuals=["wooden_blocks", "india_gate_drawing", "other_buildings"]),
    "prism_pyramid": T(
        "tool_prism_or_pyramid", "Prism or Pyramid", 2,
        "Students name the face shape all prisms share and the faces all pyramids share, and decide whether a cube is also a prism.",
        visuals=["prisms", "pyramids"]),
    "faces_edges": T(
        "tool_faces_corners_and_edges", "Faces, Corners and Edges", 3,
        "Students count the faces, edges and corners of solids, find F+V−E for each and sort solids by flat faces and straight edges.",
        visuals=["straws_and_clay", "prisms", "pyramids"]),
    "opposite": T(
        "tool_opposite_faces", "Opposite Faces", 4,
        "Students find the face opposite a given face and the faces that share an edge with it, on a die and a coloured cube.",
        visuals=["die", "colour_cube"]),
    "spot_faces": T(
        "tool_spot_the_faces", "Spot the Faces", 5,
        "Students mark everyday objects by their faces and corners: rectangular, triangular or curved faces, and no corners.",
        visuals=["border_objects"]),
    "sort_solids": T(
        "tool_sort_the_solids", "Sort the Solids", 6,
        "Students sort solids into two circles by a rule and place a solid that fits both rules in the overlap of two circles.",
        visuals=["sorting_circles", "solid_pictures", "sphere", "prisms", "pyramids"]),
    "cubes": T(
        "tool_build_and_draw_cubes", "Build and Draw Cubes", 7,
        "Students build cube models, count the cubes in a tower including the hidden ones and complete cube drawings on triangular dot paper.",
        visuals=["cube_models", "cube_towers", "triangular_dot_paper"]),
    "riddles": T(
        "tool_solid_riddles", "Solid Riddles", 8,
        "Students pick or build the solid that fits clues about its faces, edges and corners, or about its straws and clay balls.",
        visuals=["solid_pictures", "sphere", "straws_and_clay"]),
    "fold_net": T(
        "tool_fold_the_net", "Fold the Net", 9,
        "Students match nets to solids, test which nets fold into a given solid and find the solid from its net pieces.",
        visuals=["box_net", "nets_and_solids", "nitesh"]),
    # ---- Module 2: angles and rigid shapes (Tools 10 to 15)
    "lines_meet": T(
        "tool_when_lines_meet", "When Lines Meet", 10,
        "Students make an angle by meeting two lines at a point, and mark and count the angles in pictures.",
        visuals=["straws_angle", "angle_mark", "yoga_figures", "house_and_boat"]),
    "right_checker": T(
        "tool_right_angle_checker", "Right Angle Checker", 11,
        "Students make a paper right angle, use it to test the corners of shapes and objects, and draw right angles on a dot grid.",
        visuals=["right_angle_checker", "dot_grid", "angle_mark"]),
    "acute_obtuse": T(
        "tool_acute_or_obtuse", "Acute or Obtuse", 12,
        "Students tell an acute angle from an obtuse angle by comparing it with a right angle, and draw and mark both kinds.",
        visuals=["dot_grid", "angle_mark", "right_angle_checker", "stick_figures"]),
    "push_straws": T(
        "tool_push_the_straw_shapes", "Push the Straw Shapes", 13,
        "Students push one side of a straw triangle and a straw rectangle and say which one keeps its shape.",
        visuals=["rigid_shapes", "straws_and_clay"]),
    "push_angles": T(
        "tool_angles_after_the_push", "Angles After the Push", 14,
        "Students push a rectangle, a square and a pentagon and say how their angles change.",
        visuals=["rigid_shapes", "straws_and_clay", "angle_mark"]),
    "shape_angles": T(
        "tool_angles_in_shapes", "Angles in Shapes", 15,
        "Students draw three- and four-sided shapes on a dot grid, count their right angles and tell shapes apart by their kinds of angles.",
        visuals=["dot_grid", "four_sided_shapes", "angle_shapes", "angle_mark"]),
    # ---- Module 3: circles and flat shapes (Tools 16 to 19)
    "circle_make": T(
        "tool_make_a_circle", "Make a Circle", 16,
        "Students form a circle from equal straws and from marked points at the same distance from a centre.",
        visuals=["equal_straws_circle"]),
    "circle_fold": T(
        "tool_fold_the_circle", "Fold the Circle", 17,
        "Students show that the folds of a circle are equal diameters through the centre and that a diameter is double the radius.",
        visuals=["circle_paper"]),
    "radius_diameter": T(
        "tool_find_radius_and_diameter", "Find Radius and Diameter", 18,
        "Students draw a circle design, mark its centre, radius and diameter and compare wheels by radius and diameter.",
        visuals=["compass_design", "carpet_design", "wheels"]),
    "sides_angles": T(
        "tool_sides_and_angles", "Sides and Angles", 19,
        "Students sort flat shapes by their sides and their angles and find that a straight-sided shape has as many angles as sides.",
        visuals=["shape_cards", "angle_shapes", "dot_grid"]),
    # ---- Module 4: shape puzzles (Tools 20 to 22)
    "divide": T(
        "tool_divide_the_shapes", "Divide the Shapes", 20,
        "Students find the hidden shapes in a drawing and draw lines that divide a shape into smaller shapes.",
        visuals=["hidden_shapes", "dissection_shapes", "dot_grid"]),
    "webs": T(
        "tool_spider_web_puzzles", "Spider Web Puzzles", 21,
        "Students count the triangles and rectangles in two webs and decide which walks can be made without using a wall twice.",
        visuals=["spider_webs", "squiggly_and_wiggly"]),
    "matchsticks": T(
        "tool_matchstick_moves", "Matchstick Moves", 22,
        "Students make, move and remove matchsticks to form a given number of triangles.",
        visuals=["matchsticks"]),
}
