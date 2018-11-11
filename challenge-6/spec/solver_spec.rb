require 'spec_helper'

RSpec.describe Solver do
  let(:class_instance) { described_class.new }

  let(:root) do
    Node.new(
      "root",
      Node.new("left", Node.new("left.left")),
      Node.new("right")
    )
  end

  let(:serialized_root) { "root left left.left - - - right - -" }

  describe "#serialize" do
    subject { class_instance.serialize(root) }

    it { is_expected.to eq(serialized_root) }
  end

  describe "#deserialize" do
    subject { class_instance.deserialize(serialized_root) }

    it { expect(class_instance.serialize(subject)).to eq(serialized_root) }
  end

  describe "serialize/deserialize" do
    subject { class_instance.deserialize(class_instance.serialize(root)) }

    it { expect(subject.left.left.val).to eq("left.left") }
  end
end
